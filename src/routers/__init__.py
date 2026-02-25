from fastapi import APIRouter
from src.routers.base import router as base_router
from src.routers.admin import router as admin_router

router = APIRouter()
router.include_router(base_router)
router.include_router(admin_router, prefix="/admin")