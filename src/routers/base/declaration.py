from fastapi import APIRouter, Depends

from src.entities.declaration import Declaration
from src.schemas.create_declaration import CreateDeclarationRequest, DeclarationResponse
from src.schemas.verify_token_response import VerifyTokenResponse
from src.services.declaration import DeclarationService
from src.utils.dependencies import require_authorized, get_declaration_service

router = APIRouter(tags=["declaration"])

@router.post("", status_code=201, response_model=DeclarationResponse,
             description="Создать заявление")
async def declaration_create(declaration_object: CreateDeclarationRequest,
                      verified: VerifyTokenResponse = Depends(require_authorized),
                      declaration_service: DeclarationService = Depends(get_declaration_service)):
    declaration_entity: Declaration = await declaration_service.create(
        user_id=verified.user_id,
        student_fullname=declaration_object.student_fullname,
        parent_fullname=declaration_object.parent_fullname,
        purpose=declaration_object.purpose,
        leave_at=declaration_object.leave_at,
        return_at=declaration_object.return_at,
        address=declaration_object.address,
        contact=declaration_object.contact
    )
    return DeclarationResponse.from_entity(declaration_entity)

@router.get("/my_recent", response_model=list[DeclarationResponse],
            description='Получить недавние заявления, поданные авторизованным пользователем')
async def declaration_get_my_recent(offset: int, limit: int, verified: VerifyTokenResponse = Depends(require_authorized), declaration_service: DeclarationService = Depends(get_declaration_service)):
    return [DeclarationResponse.from_entity(entity) for entity in await declaration_service.get_recent_by_user_id(user_id=verified.user_id, offset=offset, limit=limit)]
