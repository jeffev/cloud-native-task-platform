import os
from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.router import router as api_router


def create_application() -> FastAPI:
    app = FastAPI(
        title="Cloud Native Task Platform",
        version="1.0.0",
    )

    # Include API v1 routes
    app.include_router(api_router)

    # Healthcheck
    @app.get("/health", tags=["health"])
    def health():
        return {"status": "ok"}

    return app


app = create_application()


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


# Avoid auto-creating tables during tests
if os.getenv("ENV") != "test":
    create_tables()
