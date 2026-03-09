from fastapi import APIRouter, Depends

from src.schemas.declaration import DeclarationResponse, DeclarationsListResponse
from src.services.declaration import DeclarationService
from src.utils.dependencies import get_declaration_service
from sesc_auth_sdk.schemas.user import UserSchema
from sesc_auth_sdk.dependencies import LyceumAuth
from sesc_auth_sdk.enums.role import Role

router = APIRouter(tags=["declaration"])

@router.get("/recent", response_model=DeclarationsListResponse,
            summary='Получить недавние заявления')
async def declaration_get_recent(offset: int, limit: int,
                                 _: UserSchema = Depends(LyceumAuth([Role.admin])),
                                 declaration_service: DeclarationService = Depends(get_declaration_service)):
    return DeclarationsListResponse(declarations=[DeclarationResponse.from_entity(entity) for entity in await declaration_service.get_recent(offset, limit)],
                                    total=await declaration_service.get_total_recent_count())
