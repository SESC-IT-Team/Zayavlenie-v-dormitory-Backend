from uuid import UUID
from datetime import datetime

class Declaration:
    def __init__(self, declaration_id: UUID, user_id: UUID,
                 student_fullname: str,
                 parent_fullname: str,
                 purpose: str,
                 leave_at: datetime,
                 return_at: datetime,
                 address: str,
                 contact: str,
                 created_at: datetime | None = None,
                 updated_at: datetime | None = None):
        self.id: UUID = declaration_id
        self.user_id: UUID = user_id

        self.student_fullname: str = student_fullname
        self.parent_fullname: str = parent_fullname
        self.purpose: str = purpose

        self.leave_at: datetime = leave_at
        self.return_at: datetime = return_at

        self.address: str = address
        self.contact: str = contact

        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at
