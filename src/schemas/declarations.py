from pydantic import BaseModel
from datetime import datetime

from src.enums.permission import Permission
from src.enums.role import Role


class Declaration(BaseModel):
    student_name: str
    student_full_name: str
    parent_name: str
    parent_full_name: str
    parent_middle_name: str
    purposes: str
    leave_date: datetime
    return_date: datetime
    adress: str
    contact: str