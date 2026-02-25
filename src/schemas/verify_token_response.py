from pydantic.v1 import BaseModel

from src.enums.permission import Permission
from src.enums.role import Role


class VerifyTokenResponse(BaseModel):
    user_id: str
    role: Role
    permissions: list[Permission]