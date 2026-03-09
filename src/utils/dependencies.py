from fastapi import Depends
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.declaration import DeclarationRepository
from src.utils.database import get_db
from src.services.declaration import DeclarationService

def get_declaration_service(db: AsyncSession = Depends(get_db)) -> DeclarationService:
    return DeclarationService(DeclarationRepository(db))

