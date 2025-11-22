# Main file for the backend application

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.analyzer import analyzeFile
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