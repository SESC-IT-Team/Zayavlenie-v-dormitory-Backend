from fastapi import APIRouter, Depends

from src.entities.declaration import Declaration
from src.schemas.declaration import CreateDeclarationRequest, DeclarationResponse, DeclarationsListResponse
from src.services.declaration import DeclarationService
from src.utils.dependencies import get_declaration_service
from sesc_auth_sdk.dependencies import LyceumAuth
from sesc_auth_sdk.schemas.user import UserSchema

router = APIRouter(tags=["declaration"])

@router.post("", status_code=201, response_model=DeclarationResponse,
             description="Создать заявление")
async def declaration_create(declaration_object: CreateDeclarationRequest,
                             user: UserSchema = Depends(LyceumAuth()),
                             declaration_service: DeclarationService = Depends(get_declaration_service)):
    declaration_entity: Declaration = await declaration_service.create(
        user_id=user.id,
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
async def declaration_get_my_recent(offset: int, limit: int, user: UserSchema = Depends(LyceumAuth()), declaration_service: DeclarationService = Depends(get_declaration_service)):
    return DeclarationsListResponse(declarations=[DeclarationResponse.from_entity(entity) for entity in await declaration_service.get_recent_by_user_id(user_id=user.id, offset=offset, limit=limit)],
                                    total=await declaration_service.get_total_recent_count_by_user_id(user_id=user.id))
