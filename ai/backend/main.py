from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(
    title="Education Academic Intelligence API",
    description="AI-powered academic intelligence backend",
    version="1.0"
)

# Allow dashboard to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dataset
DATA_FILE = "../data/feature_engineered_data.csv"

df = pd.read_csv(DATA_FILE)


# Home
@app.get("/")
def home():
    return {
        "message": "Education Academic Intelligence API is running"
    }


# Student AI Insights
@app.get("/api/ai/student/{student_id}/insights")
def student_insights(student_id: str):

    student = df[df["student_id"] == student_id]

    if student.empty:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    attendance = student["attendance_percentage"].mean()
    assignment = student["assignment_average"].mean()
    exam = student["exam_average"].mean()
    trend = student["performance_trend"].mean()
    overall = student["overall_score"].mean()

    # Weak subjects
    weak_subjects = student[
        student["exam_average"] < 50
    ]["subject"].tolist()

    # Risk factors
    risk_factors = []

    if attendance < 75:
        risk_factors.append(
            f"Low attendance ({attendance:.1f}%)"
        )

    if assignment < 50:
        risk_factors.append(
            f"Low assignment performance ({assignment:.1f})"
        )

    if exam < 50:
        risk_factors.append(
            f"Low exam performance ({exam:.1f})"
        )

    if trend < 0:
        risk_factors.append(
            f"Declining performance ({trend:.1f})"
        )

    # Risk level
    if len(risk_factors) >= 3:
        risk_level = "HIGH"
    elif len(risk_factors) >= 1:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # Recommendations
    recommendations = []

    if attendance < 75:
        recommendations.append(
            "Improve attendance in upcoming classes"
        )

    if assignment < 50:
        recommendations.append(
            "Complete and practice assignments"
        )

    if exam < 50:
        recommendations.append(
            "Practice examination topics regularly"
        )

    if trend < 0:
        recommendations.append(
            "Monitor declining performance"
        )

    if not recommendations:
        recommendations.append(
            "Continue the current learning pattern"
        )

    return {
        "student_id": student_id,
        "risk_level": risk_level,
        "overall_score": round(overall, 2),
        "attendance_percentage": round(attendance, 2),
        "assignment_average": round(assignment, 2),
        "exam_average": round(exam, 2),
        "performance_trend": round(trend, 2),
        "weak_subjects": weak_subjects,
        "risk_factors": risk_factors,
        "recommendations": recommendations
    }
# -------------------------
# ADMIN DASHBOARD OVERVIEW
# -------------------------

@app.get("/api/admin/overview")
def admin_overview():

    total_students = df["student_id"].nunique()

    low_risk = 0
    medium_risk = 0
    high_risk = 0

    low_attendance = 0
    declining_students = 0

    weak_subject_counts = {}

    for student_id, student in df.groupby("student_id"):

        attendance = student["attendance_percentage"].mean()
        assignment = student["assignment_average"].mean()
        exam = student["exam_average"].mean()
        trend = student["performance_trend"].mean()

        risk_count = 0

        if attendance < 75:
            risk_count += 1

        if assignment < 50:
            risk_count += 1

        if exam < 50:
            risk_count += 1

        if trend < 0:
            risk_count += 1

        if risk_count >= 3:
            high_risk += 1

        elif risk_count >= 1:
            medium_risk += 1

        else:
            low_risk += 1

        if attendance < 75:
            low_attendance += 1

        if trend < 0:
            declining_students += 1

        # Weak subjects
        weak = student[
            student["exam_average"] < 50
        ]["subject"].tolist()

        for subject in weak:

            weak_subject_counts[subject] = (
                weak_subject_counts.get(subject, 0) + 1
            )

    return {
        "total_students": total_students,
        "low_risk_students": low_risk,
        "medium_risk_students": medium_risk,
        "high_risk_students": high_risk,
        "low_attendance_students": low_attendance,
        "declining_performance_students": declining_students,
        "weak_subjects": weak_subject_counts
    }