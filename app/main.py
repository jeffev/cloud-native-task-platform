import structlog
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.logging_config import configure_logging
from app.observability.middleware import ObservabilityMiddleware

# Configure structured logging
configure_logging()
logger = structlog.get_logger()

app = FastAPI(
    title="Cloud Native Task Platform",
    version="1.0.0"
)

# -----------------------------
# Prometheus default metrics
# -----------------------------
Instrumentator().instrument(app).expose(app)

# -----------------------------
# Middlewares
# -----------------------------
app.add_middleware(ObservabilityMiddleware)

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
