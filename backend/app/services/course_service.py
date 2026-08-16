from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate


def create_course(
    db: Session,
    teacher_id: int,
    course_data: CourseCreate
):
    course = Course(
        name=course_data.name,
        code=course_data.code,
        description=course_data.description,
        department=course_data.department,
        credits=course_data.credits,
        teacher_id=teacher_id
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_teacher_courses(
    db: Session,
    teacher_id: int
):
    return (
        db.query(Course)
        .filter(Course.teacher_id == teacher_id)
        .all()
    )


def get_course(
    db: Session,
    course_id: int
):
    return (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )


def update_course(
    db: Session,
    course_id: int,
    teacher_id: int,
    course_data: CourseCreate
):
    course = (
        db.query(Course)
        .filter(
            Course.id == course_id,
            Course.teacher_id == teacher_id
        )
        .first()
    )

    if course is None:
        return None

    course.name = course_data.name
    course.code = course_data.code
    course.description = course_data.description
    course.department = course_data.department
    course.credits = course_data.credits

    db.commit()
    db.refresh(course)

    return course


def delete_course(
    db: Session,
    course_id: int,
    teacher_id: int
):
    course = (
        db.query(Course)
        .filter(
            Course.id == course_id,
            Course.teacher_id == teacher_id
        )
        .first()
    )

    if course is None:
        return None

    db.delete(course)
    db.commit()

    return course