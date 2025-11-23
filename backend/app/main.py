# Main file for the backend application

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.analyzer import analyzeFile
from app.hide import hideStringInImage, extractStringFromImage
import os
import uuid

app = FastAPI()

UPLOAD_DIRECTORY = "/tmp/uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

origins = [
    "http://localhost:3000",  # ton frontend
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] pour tout autoriser en dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scan")
async def scan(file: UploadFile = File(...)):
    
    # Save the uploaded file temporarily
    fileId = str(uuid.uuid4())
    filePath = os.path.join(UPLOAD_DIRECTORY, fileId + "_" + file.filename)

    with open(filePath, "wb") as f:
        content = await file.read()
        f.write(content)

    # Analyze the file
    analysisResult = analyzeFile(filePath)

    # Clean up the uploaded file
    os.remove(filePath)

    return analysisResult

@app.post("/hide")
async def hide(image: UploadFile = File(...), message: str = ""):
    # Save the uploaded image temporarily
    imageId = str(uuid.uuid4())
    imagePath = os.path.join(UPLOAD_DIRECTORY, imageId + "_" + image.filename)
    outputImagePath = os.path.join(UPLOAD_DIRECTORY, imageId + "_encoded_" + image.filename)

    with open(imagePath, "wb") as f:
        content = await image.read()
        f.write(content)

    # Hide the message in the image
    hideStringInImage(imagePath, message, outputImagePath)

    # Read the modified image to return
    with open(outputImagePath, "rb") as f:
        encodedImageContent = f.read()

    # Clean up the uploaded and encoded images
    os.remove(imagePath)
    os.remove(outputImagePath)

    return {
        "filename": "encoded_" + image.filename,
        "content": encodedImageContent
    }


@app.post("/extract")
async def extract(image: UploadFile = File(...)):
    # Save the uploaded image temporarily
    imageId = str(uuid.uuid4())
    imagePath = os.path.join(UPLOAD_DIRECTORY, imageId + "_" + image.filename)

    with open(imagePath, "wb") as f:
        content = await image.read()
        f.write(content)

    # Extract the hidden message from the image
    secretMessage = extractStringFromImage(imagePath)

    # Clean up the uploaded image
    os.remove(imagePath)

    return {
        "message": secretMessage
    }