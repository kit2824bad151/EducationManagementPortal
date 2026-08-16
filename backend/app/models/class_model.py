from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    section = Column(String(20), nullable=True)

    academic_year = Column(String(20), nullable=True)

    room_number = Column(String(50), nullable=True)