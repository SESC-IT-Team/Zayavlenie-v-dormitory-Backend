from datetime import datetime
from uuid import UUID, uuid4

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from src.entities.declaration import Declaration
from src.repositories.declaration import DeclarationRepository
from src.utils.database import get_db


class DeclarationService:
    def __init__(self, repository: DeclarationRepository):
        self._repo = repository

    async def get_by_id(self, declaration_id: UUID) -> Declaration | None:
        return await self._repo.get_by_id(declaration_id)

    async def create(self, user_id: UUID, student_fullname: str,
                     parent_fullname: str, purpose: str,
                     leave_at: datetime, return_at: datetime,
                     address: str, contact: str) -> Declaration | None:
        declaration = Declaration(uuid4(), user_id, student_fullname,
                                  parent_fullname, purpose, leave_at,
                                  return_at, address, contact)
        return await self._repo.create(declaration)

    async def get_list_by_user_id(self, user_id: UUID, offset: int,
                                  limit: int) -> list[Declaration]:
        return await self._repo.get_list_by_user_id(user_id, offset, limit)

def get_declaration_service(db: AsyncSession = Depends(get_db)) -> DeclarationService:
    return DeclarationService(DeclarationRepository(db))
