from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    department: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    credits: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True
    )

    teacher_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("teachers.id"),
        nullable=True
    )

    teacher = relationship(
        "Teacher",
        back_populates="courses"
    )