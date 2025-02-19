from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = FastAPI()

logging.basicConfig(level=logging.INFO)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(agent_host_name="jaeger", agent_port=6831)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


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
