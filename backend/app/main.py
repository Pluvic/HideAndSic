# Main file for the backend application

from fastapi import FastAPI
import os

app = FastAPI()

UPLOAD_DIRECTORY = "/tmp/uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/scan")
async def scan(file):
    # To implement
    return 0