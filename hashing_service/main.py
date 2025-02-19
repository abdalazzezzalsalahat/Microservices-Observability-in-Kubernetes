from fastapi import FastAPI
import hashlib


app = FastAPI()


@app.post("/hash")
async def generate_hash(data: dict):
    input_text = data.get("text", "")
    sha256_hash = hashlib.sha256(input_text.encode()).hexdigest()
    return {"hash": sha256_hash}
