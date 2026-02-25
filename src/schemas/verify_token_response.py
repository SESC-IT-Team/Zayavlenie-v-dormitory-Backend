from uuid import UUID

from pydantic.v1 import BaseModel

from src.enums.permission import Permission
from src.enums.role import Role


class VerifyTokenResponse(BaseModel):
    user_id: UUID
    role: Role
    permissions: list[Permission]