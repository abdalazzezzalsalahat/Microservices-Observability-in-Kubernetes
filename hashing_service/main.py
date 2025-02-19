from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

Instrumentator().instrument(app).expose(app)

logging.basicConfig(level=logging.INFO)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(agent_host_name="jaeger", agent_port=6831)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


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
