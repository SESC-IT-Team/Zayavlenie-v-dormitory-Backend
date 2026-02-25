from fastapi import APIRouter
from src.routers.base.auth import router as auth_router

router = APIRouter()
router.include_router(auth_router)

__all__ = ["router"]