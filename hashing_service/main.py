from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


class HashRequest(BaseModel):
    text: str


@app.post("/hash")
async def generate_hash(request: HashRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input cannot be empty")

    sha256_hash = hashlib.sha256(request.text.encode()).hexdigest()

    logging.info(f"Generated hash for input: {request.text}")

    return {"hash": sha256_hash}


@app.get("/health")
async def health():
    return {"status": "ok"}
