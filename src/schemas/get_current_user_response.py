from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from src.enums.role import Role


class GetCurrentUserResponse(BaseModel):
    id: UUID
    last_name: str
    first_name: str
    middle_name: str | None
    role: Role
    class_name: str | None
    login: str
    created_at: datetime
    updated_at: datetime
