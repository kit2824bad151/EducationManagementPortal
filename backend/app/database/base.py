from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
from app.models.user import User
from app.models.teacher import Teacher
from app.models.student import Student
from app.models.course import Course
from app.models.class_model import Class