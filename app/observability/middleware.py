import time
import uuid
import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.observability.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
    ERROR_COUNT,
)

logger = structlog.get_logger()


class ObservabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Generate request ID
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        logger.info(
            "request_started",
            path=request.url.path,
            method=request.method,
            request_id=request_id,
        )

        response = await call_next(request)

        duration = time.time() - start_time

        # Prometheus metrics
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status_code=response.status_code,
        ).inc()

        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path,
        ).observe(duration)

        if response.status_code >= 500:
            ERROR_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
            ).inc()

        logger.info(
            "request_finished",
            path=request.url.path,
            method=request.method,
            status_code=response.status_code,
            duration_ms=round(duration * 1000, 2),
            request_id=request_id,
        )

        response.headers["X-Request-ID"] = request_id

        return response
