from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True
    )

    phone: Mapped[Optional[str]] = mapped_column(
        String(20),
        nullable=True
    )

    qualification: Mapped[Optional[str]] = mapped_column(
        String(200),
        nullable=True
    )

    department: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    courses = relationship(
        "Course",
        back_populates="teacher"
    )