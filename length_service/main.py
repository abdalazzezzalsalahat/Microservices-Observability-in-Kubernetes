from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


class LengthRequest(BaseModel):
    text: str


@app.post("/length")
async def calculate_length(request: LengthRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input cannot be empty")

    text_length = len(request.text)

    logging.info(f"Calculated length: {text_length} for input: {request.text}")

    return {"length": text_length}


@app.get("/health")
async def health():
    return {"status": "ok"}
