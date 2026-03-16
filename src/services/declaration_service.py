from datetime import datetime
from uuid import UUID, uuid4


from src.entities.declaration_entity import DeclarationEntity
from src.repositories.declaration_repository import DeclarationRepository


class DeclarationService:
    def __init__(self, repository: DeclarationRepository):
        self._repo: DeclarationRepository = repository

    async def get_by_id(self, declaration_id: UUID) -> DeclarationEntity | None:
        return await self._repo.get_by_id(declaration_id)

    async def create(self, user_id: UUID, student_fullname: str,
                     parent_fullname: str, purpose: str,
                     leave_at: datetime, return_at: datetime,
                     address: str, contact: str) -> DeclarationEntity | None:
        declaration = DeclarationEntity(id=uuid4(), user_id=user_id, student_fullname=student_fullname,
                                        parent_fullname=parent_fullname, purpose=purpose, leave_at=leave_at,
                                        return_at=return_at, address=address, contact=contact)
        return await self._repo.create(declaration)

    async def get_recent_by_user_id(self, user_id: UUID, offset: int,
                                    limit: int) -> list[DeclarationEntity]:
        return await self._repo.get_list_by_user_id(user_id, offset, limit)

    async def get_recent(self, offset: int,
                         limit: int) -> list[DeclarationEntity]:
        return await self._repo.get_list(offset, limit)

    async def get_total_recent_count(self) -> int:
        return await self._repo.get_total_count()

    async def get_total_recent_count_by_user_id(self, user_id: UUID) -> int:
        return await self._repo.get_total_count_by_user_id(user_id=user_id)

