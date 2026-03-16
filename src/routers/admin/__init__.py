from fastapi import APIRouter
from src.routers.admin.admin_declaration_router import router as declaration_router

router = APIRouter(tags=["admin"])

router.include_router(declaration_router, prefix="/declaration", )

__all__ = ["router"]