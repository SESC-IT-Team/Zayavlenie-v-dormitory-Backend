from pydantic import BaseModel
from datetime import datetime

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