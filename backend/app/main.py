from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from fastapi import FastAPI

from app.core.config import settings
from app.database.base import Base
from app.database.connection import engine

from app import models
from app.routes.teacher import router as teacher_router
from app.routes.course import router as course_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(teacher_router)
app.include_router(course_router)

@app.get("/")
def root():
    return {
        "message": "Education Management Portal API"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "message": "API is running"
    }
@app.get("/api/health/database")
def database_health(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        result.fetchone()

        return {
            "status": "success",
            "message": "Database connection is working"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
