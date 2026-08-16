from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.course import CourseCreate, CourseResponse
from app.services.course_service import (
    create_course,
    get_teacher_courses,
    update_course,
    delete_course,
)


router = APIRouter(
    prefix="/api/teachers",
    tags=["Teacher Courses"]
)


@router.post(
    "/{teacher_id}/courses",
    response_model=CourseResponse
)
def create_teacher_course(
    teacher_id: int,
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    return create_course(
        db,
        teacher_id,
        course_data
    )


@router.get(
    "/{teacher_id}/courses",
    response_model=list[CourseResponse]
)
def get_courses_for_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    return get_teacher_courses(
        db,
        teacher_id
    )


@router.put(
    "/{teacher_id}/courses/{course_id}",
    response_model=CourseResponse
)
def update_teacher_course(
    teacher_id: int,
    course_id: int,
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    course = update_course(
        db,
        course_id,
        teacher_id,
        course_data
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found for this teacher"
        )

    return course


@router.delete(
    "/{teacher_id}/courses/{course_id}"
)
def delete_teacher_course(
    teacher_id: int,
    course_id: int,
    db: Session = Depends(get_db)
):
    course = delete_course(
        db,
        course_id,
        teacher_id
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found for this teacher"
        )

    return {
        "status": "success",
        "message": "Course deleted successfully"
    }