from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate


def create_teacher(db: Session, teacher_data: TeacherCreate):
    teacher = Teacher(
        name=teacher_data.name,
        email=teacher_data.email,
        phone=teacher_data.phone,
        qualification=teacher_data.qualification,
        department=teacher_data.department,
    )

    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    return teacher


def get_teachers(db: Session):
    return db.query(Teacher).all()


def get_teacher(db: Session, teacher_id: int):
    return (
        db.query(Teacher)
        .filter(Teacher.id == teacher_id)
        .first()
    )


def update_teacher(
    db: Session,
    teacher_id: int,
    teacher_data: TeacherCreate
):
    teacher = get_teacher(db, teacher_id)

    if teacher is None:
        return None

    teacher.name = teacher_data.name
    teacher.email = teacher_data.email
    teacher.phone = teacher_data.phone
    teacher.qualification = teacher_data.qualification
    teacher.department = teacher_data.department

    db.commit()
    db.refresh(teacher)

    return teacher


def delete_teacher(db: Session, teacher_id: int):
    teacher = get_teacher(db, teacher_id)

    if teacher is None:
        return None

    db.delete(teacher)
    db.commit()

    return teacher