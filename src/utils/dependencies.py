from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.enums import role
from src.enums.role import Role
from src.repositories.declaration import DeclarationRepository
from src.schemas.verify_token_response import VerifyTokenResponse
from src.services.auth import AuthService
from src.utils.database import get_db
from src.services.declaration import DeclarationService

security_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)

def get_declaration_service(db: AsyncSession = Depends(get_db)) -> DeclarationService:
    return DeclarationService(DeclarationRepository(db))

async def require_authorized(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)) -> VerifyTokenResponse:
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return await AuthService.verify_token(credentials.credentials)

async def require_admin(verified: VerifyTokenResponse = Depends(require_authorized)):
    if verified.role != Role.admin:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Admin only.")
    return verified

