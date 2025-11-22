# Main file for the backend application

from fastapi import FastAPI
from app.analyzer import analyzeFile
import os
import uuid

app = FastAPI()

UPLOAD_DIRECTORY = "/tmp/uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/scan")
async def scan(file):
    
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