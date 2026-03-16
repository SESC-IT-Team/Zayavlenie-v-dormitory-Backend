from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class DeclarationEntity(BaseModel):
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
