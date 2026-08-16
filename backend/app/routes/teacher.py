from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.teacher import Teacher


router = APIRouter(
    prefix="/api/teachers",
    tags=["Teachers"]
)


@router.get("/")
def get_all_teachers(
    db: Session = Depends(get_db)
):
    teachers = db.query(Teacher).all()

    return teachers


@router.get("/{teacher_id}")
def get_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = (
        db.query(Teacher)
        .filter(Teacher.id == teacher_id)
        .first()
    )

    if teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher