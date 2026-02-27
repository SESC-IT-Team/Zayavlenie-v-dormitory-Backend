from uuid import UUID

from pydantic import BaseModel
from datetime import datetime

from src.entities.declaration import Declaration


class CreateDeclarationRequest(BaseModel):
    student_fullname: str
    parent_fullname: str
    purpose: str

    leave_at: datetime
    return_at: datetime

    address: str
    contact: str

class DeclarationResponse(BaseModel):
    id: UUID
    user_id: UUID
    student_fullname: str
    parent_fullname: str
    purpose: str

    leave_at: datetime
    return_at: datetime

    address: str
    contact: str

    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: Declaration):
        return cls(id=entity.id, user_id=entity.user_id,
                   student_fullname=entity.student_fullname,
                   parent_fullname=entity.parent_fullname,
                   purpose=entity.purpose,
                   leave_at=entity.leave_at,
                   return_at=entity.return_at,
                   address=entity.address,
                   contact=entity.contact,
                   created_at=entity.created_at,
                   updated_at=entity.updated_at)