from fastapi import APIRouter, Depends

from src.schemas.declaration import DeclarationResponse, DeclarationsListResponse
from src.schemas.verify_token_response import VerifyTokenResponse
from src.services.declaration import DeclarationService
from src.utils.dependencies import require_admin, get_declaration_service

router = APIRouter(tags=["declaration"])

@router.get("/recent", response_model=DeclarationsListResponse,
            summary='Получить недавние заявления')
async def declaration_get_recent(offset: int, limit: int,
                                 _: VerifyTokenResponse = Depends(require_admin),
                                 declaration_service: DeclarationService = Depends(get_declaration_service)):
    return DeclarationsListResponse(declarations=[DeclarationResponse.from_entity(entity) for entity in await declaration_service.get_recent(offset, limit)],
                                    total=await declaration_service.get_total_recent_count())
