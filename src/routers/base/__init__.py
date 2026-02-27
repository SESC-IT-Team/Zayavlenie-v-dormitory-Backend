from fastapi import APIRouter
from src.routers.base.declaration import router as declaration_router

router = APIRouter()

router.include_router(declaration_router, prefix="/declaration")

__all__ = ["router"]