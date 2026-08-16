from pydantic import BaseModel, EmailStr
from typing import Optional


class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    qualification: Optional[str] = None
    department: Optional[str] = None


class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    qualification: Optional[str] = None
    department: Optional[str] = None

    class Config:
        from_attributes = True