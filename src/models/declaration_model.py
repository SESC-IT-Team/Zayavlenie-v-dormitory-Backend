import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, String, Integer, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class DeclarationModel(Base):
    __tablename__ = "declarations"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True))

    student_fullname: Mapped[str] = mapped_column(String(255), nullable=False)
    parent_fullname: Mapped[str] = mapped_column(String(255), nullable=False)
    purpose: Mapped[str] = mapped_column(String(255), nullable=False)

    leave_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    return_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    address: Mapped[str] = mapped_column(String(255), nullable=False)
    contact: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)