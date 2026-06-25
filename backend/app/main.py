from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
)

app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "status": "running",
    }