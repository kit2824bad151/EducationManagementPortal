import pandas as pd

# Load feature-engineered dataset
df = pd.read_csv("data/feature_engineered_data.csv")

print("\nAI INSIGHTS")
print("===========")

# Group subjects for each student
for student_id, student_data in df.groupby("student_id"):

    # Average values for the student
    attendance = student_data["attendance_percentage"].mean()
    assignment = student_data["assignment_average"].mean()
    exam = student_data["exam_average"].mean()
    trend = student_data["performance_trend"].mean()
    overall = student_data["overall_score"].mean()

    # Find weak subjects
    weak_subjects = student_data[
        student_data["exam_average"] < 50
    ]["subject"].tolist()

    # Calculate risk factors
    risk_factors = []

    if attendance < 75:
        risk_factors.append(f"Low attendance ({attendance:.1f}%)")

    if assignment < 50:
        risk_factors.append(f"Low assignment performance ({assignment:.1f})")

    if exam < 50:
        risk_factors.append(f"Low exam performance ({exam:.1f})")

    if trend < 0:
        risk_factors.append(
            f"Declining performance ({trend:.1f})"
        )

    # Determine risk level
    if len(risk_factors) >= 3:
        risk_level = "HIGH"
    elif len(risk_factors) >= 1:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print(f"\nStudent {student_id}")
    print("--------------------")
    print(f"Risk Level: {risk_level}")
    print(f"Overall Score: {overall:.1f}")
    print(f"Attendance: {attendance:.1f}%")
    print(f"Exam Average: {exam:.1f}")
    print(f"Performance Trend: {trend:+.1f}")

    print("\nMain contributing factors:")

    if risk_factors:
        for factor in risk_factors:
            print(f"- {factor}")
    else:
        print("- No major risk factors identified")

    print("\nWeak Subjects:")

    if weak_subjects:
        for subject in weak_subjects:
            print(f"- {subject}")
    else:
        print("- None")

    print("\nAI Recommendation:")

    if risk_level == "HIGH":
        print("- Immediate academic intervention is recommended.")
        print("- Improve attendance and examination preparation.")

    elif risk_level == "MEDIUM":
        print("- Monitor academic progress regularly.")
        print("- Focus on identified weak areas.")

    else:
        print("- Continue the current learning pattern.")
        print("- Maintain regular academic performance.")

print("\nAI insights generated successfully!")