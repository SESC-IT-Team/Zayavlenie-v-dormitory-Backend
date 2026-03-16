from fastapi import APIRouter
from src.routers.base.base_declaration_router import router as declaration_router

router = APIRouter()

router.include_router(declaration_router, prefix="/declaration")

__all__ = ["router"]