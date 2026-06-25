from fastapi import APIRouter

from app.api.commands import router as commands_router

router = APIRouter()

router.include_router(commands_router)


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "NAMI Backend",
        "version": "0.1.0",
    }