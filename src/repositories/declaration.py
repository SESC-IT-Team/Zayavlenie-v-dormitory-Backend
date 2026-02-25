from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.declaration import DeclarationModel
from src.entities.declaration import Declaration


class DeclarationRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    def _to_entity(self, m: DeclarationModel) -> Declaration:
        return Declaration(
            declaration_id=m.id,
            user_id=m.user_id,
            student_fullname=m.student_fullname,
            parent_fullname=m.parent_fullname,
            purpose=m.purpose,
            leave_at=m.leave_at,
            return_at=m.return_at,
            address=m.address,
            contact=m.contact,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    async def get_by_id(self, declaration_id: UUID) -> Declaration | None:
        result = await self._session.execute(select(DeclarationModel).where(DeclarationModel.id == declaration_id))
        row = result.scalar_one_or_none()
        return self._to_entity(row) if row else None

    async def create(self, declaration: Declaration) -> Declaration:
        m = DeclarationModel(
            id=declaration.id,
            user_id=declaration.user_id,
            student_fullname=declaration.student_fullname,
            parent_fullname=declaration.parent_fullname,
            purpose=declaration.purpose,
            leave_at=declaration.leave_at,
            return_at=declaration.return_at,
            address=declaration.address,
            contact=declaration.contact,
            created_at=declaration.created_at,
            updated_at=declaration.updated_at
        )
        self._session.add(m)
        await self._session.flush()
        await self._session.refresh(m)
        return self._to_entity(m)

    async def get_list_by_user_id(self, user_id: UUID, offset: int, limit: int) -> list[Declaration]:
        result = await self._session.execute(
            select(DeclarationModel).where(DeclarationModel.user_id == user_id).order_by(DeclarationModel.created_at.desc()).offset(offset).limit(limit)
        )
        return [self._to_entity(m) for m in result.scalars().all()]
