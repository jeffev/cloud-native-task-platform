import structlog
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.logging_config import configure_logging
from app.observability.middleware import ObservabilityMiddleware
from app.api.v1.endpoints import tasks
from app.core.database import engine, Base

# Importa models para registrar no metadata
from app.models import task  # noqa: F401


# ---------------------------------
# Logging
# ---------------------------------
configure_logging()
logger = structlog.get_logger()


# ---------------------------------
# Lifespan (startup/shutdown)
# ---------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("starting_application")

    # cria tabelas automaticamente (dev mode)
    Base.metadata.create_all(bind=engine)

    yield

    logger.info("shutting_down_application")


# ---------------------------------
# App
# ---------------------------------
app = FastAPI(
    title="Cloud Native Task Platform",
    version="1.0.0",
    lifespan=lifespan,
)

# ---------------------------------
# Prometheus default metrics
# ---------------------------------
Instrumentator().instrument(app).expose(app)

# ---------------------------------
# Middlewares
# ---------------------------------
app.add_middleware(ObservabilityMiddleware)

# ---------------------------------
# Task Endpoints
# ---------------------------------
app.include_router(
    tasks.router,
    prefix="/api/v1"
)

# ---------------------------------
# Health Endpoints
# ---------------------------------
@app.get("/health/live")
async def liveness():
    return {"status": "alive"}


@app.get("/health/ready")
async def readiness():
    return {"status": "ready"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# ---------------------------------
# Root
# ---------------------------------
@app.get("/")
async def root():
    return {
        "service": "cloud-native-task-platform",
        "version": "1.0.0"
    }
