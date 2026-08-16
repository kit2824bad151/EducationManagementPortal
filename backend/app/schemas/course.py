from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    department: Optional[str] = None
    credits: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    description: Optional[str] = None
    department: Optional[str] = None
    credits: Optional[int] = None
    teacher_id: Optional[int] = None

    class Config:
        from_attributes = True