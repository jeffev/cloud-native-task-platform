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
        start_time = time.perf_counter()
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        try:
            logger.info(
                "request_started",
                method=request.method,
                path=request.url.path,
                request_id=request_id,
            )

            response = await call_next(request)
            status_code = response.status_code

        except Exception as exc:
            duration = time.perf_counter() - start_time

            ERROR_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
            ).inc()

            REQUEST_LATENCY.labels(
                method=request.method,
                endpoint=request.url.path,
            ).observe(duration)

            logger.error(
                "request_failed",
                method=request.method,
                path=request.url.path,
                duration_ms=round(duration * 1000, 2),
                request_id=request_id,
                error=str(exc),
            )

            raise

        duration = time.perf_counter() - start_time

        # Metrics
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status_code=status_code,
        ).inc()

        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path,
        ).observe(duration)

        if status_code >= 500:
            ERROR_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
            ).inc()

        logger.info(
            "request_finished",
            method=request.method,
            path=request.url.path,
            status_code=status_code,
            duration_ms=round(duration * 1000, 2),
            request_id=request_id,
        )

        response.headers["X-Request-ID"] = request_id

        return response
