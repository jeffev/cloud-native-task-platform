import uuid
import structlog
from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.logging_config import configure_logging

# Configure structured logging
configure_logging()
logger = structlog.get_logger()

app = FastAPI(
    title="Cloud Native Task Platform",
    version="1.0.0"
)

# -----------------------------
# Prometheus Metrics (FIXED)
# -----------------------------
Instrumentator().instrument(app).expose(app)


# -----------------------------
# Request ID Middleware
# -----------------------------
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    return response


# -----------------------------
# Logging Middleware
# -----------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        "request_started",
        path=request.url.path,
        method=request.method,
    )

    response = await call_next(request)

    logger.info(
        "request_finished",
        path=request.url.path,
        method=request.method,
        status_code=response.status_code,
        request_id=request.state.request_id,
    )

    return response


# -----------------------------
# Health Endpoints
# -----------------------------
@app.get("/health/live")
async def liveness():
    return {"status": "alive"}


@app.get("/health/ready")
async def readiness():
    return {"status": "ready"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# -----------------------------
# Root
# -----------------------------
@app.get("/")
async def root():
    return {
        "service": "cloud-native-task-platform",
        "version": "1.0.0"
    }
