import pandas as pd

# Load processed academic dataset
df = pd.read_csv("data/processed_academic_data.csv")

print("\nRECOMMENDATION ENGINE")
print("=====================")

for index, row in df.iterrows():

    student_id = row["student_id"] if "student_id" in df.columns else f"S{index+1:03d}"

    recommendations = []

    # Check attendance
    if "attendance" in df.columns and row["attendance"] < 75:
        recommendations.append("Improve attendance")

    # Check marks
    if "marks" in df.columns:
        if row["marks"] < 50:
            recommendations.append("Practice academic subjects regularly")
        elif row["marks"] < 70:
            recommendations.append("Improve subject performance")

    # Check risk level
    if "risk" in df.columns:
        risk = str(row["risk"]).lower()

        if risk == "high":
            recommendations.append("Attend additional coaching sessions")
            recommendations.append("Follow a daily study plan")

        elif risk == "medium":
            recommendations.append("Increase study time")

        elif risk == "low":
            recommendations.append("Continue current study routine")

    # Default recommendation
    if not recommendations:
        recommendations.append("Continue current academic performance")

    print(f"\nStudent {student_id}")
    print("Recommendations:")

    for recommendation in recommendations:
        print(f"- {recommendation}")

print("\nRecommendation engine completed!")