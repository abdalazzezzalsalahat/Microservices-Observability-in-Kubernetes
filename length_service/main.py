from fastapi import FastAPI


app = FastAPI()


@app.post("/length")
async def calculate_length(data: dict):

    input_text = data.get("text", "")

    return {"length": len(input_text)}
