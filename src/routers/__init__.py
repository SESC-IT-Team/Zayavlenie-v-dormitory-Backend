from fastapi import APIRouter
from src.routers.base import router as base_router
from src.routers.admin import router as admin_router
from src.routers.health import router as health_router


router = APIRouter()
router.include_router(base_router)
router.include_router(admin_router, prefix="/admin")
router.include_router(health_router, prefix="/health")