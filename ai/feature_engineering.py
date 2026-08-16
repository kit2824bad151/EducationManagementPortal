import pandas as pd
import numpy as np
import os

# ==============================
# FEATURE ENGINEERING
# ==============================

INPUT_FILE = "data/processed_academic_data.csv"
OUTPUT_FILE = "data/feature_engineered_data.csv"

# Load processed dataset
df = pd.read_csv(INPUT_FILE)

print("\nFEATURE ENGINEERING")
print("===================")

# ------------------------------
# 1. Validate required columns
# ------------------------------

required_columns = [
    "student_id",
    "attendance_percentage",
    "assignment_average",
    "assignment_completion",
    "exam_average",
    "previous_performance",
    "recent_performance",
    "subject"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print("\nMissing columns:")
    for col in missing_columns:
        print("-", col)

    print("\nFeature engineering stopped.")
    print("Please check your dataset column names.")
    exit()

print("All required columns are available.")

# ------------------------------
# 2. Convert numeric columns
# ------------------------------

numeric_columns = [
    "attendance_percentage",
    "assignment_average",
    "assignment_completion",
    "exam_average",
    "previous_performance",
    "recent_performance"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# ------------------------------
# 3. Handle missing values
# ------------------------------

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

print("Missing numeric values handled.")

# ------------------------------
# 4. Performance Trend
# ------------------------------
# Formula:
# recent performance - previous performance

df["performance_trend"] = (
    df["recent_performance"] -
    df["previous_performance"]
)

# ------------------------------
# 5. Overall Score
# ------------------------------
# Weighted academic score:
#
# Exam                = 40%
# Assignment average  = 25%
# Assignment completion = 15%
# Attendance           = 20%

df["overall_score"] = (
    df["exam_average"] * 0.40
    + df["assignment_average"] * 0.25
    + df["assignment_completion"] * 0.15
    + df["attendance_percentage"] * 0.20
)

# ------------------------------
# 6. Attendance Risk
# ------------------------------

df["attendance_risk"] = np.where(
    df["attendance_percentage"] < 75,
    1,
    0
)

# ------------------------------
# 7. Assignment Risk
# ------------------------------

df["assignment_risk"] = np.where(
    (df["assignment_average"] < 50) |
    (df["assignment_completion"] < 75),
    1,
    0
)

# ------------------------------
# 8. Examination Risk
# ------------------------------

df["exam_risk"] = np.where(
    df["exam_average"] < 50,
    1,
    0
)

# ------------------------------
# 9. Declining Performance
# ------------------------------

df["declining_performance"] = np.where(
    df["performance_trend"] < 0,
    1,
    0
)

# ------------------------------
# 10. Risk Factor Count
# ------------------------------

df["risk_factor_count"] = (
    df["attendance_risk"]
    + df["assignment_risk"]
    + df["exam_risk"]
    + df["declining_performance"]
)

# ------------------------------
# 11. Save feature-engineered data
# ------------------------------

os.makedirs("data", exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

# ------------------------------
# 12. Display results
# ------------------------------

print("\nFeature engineering completed successfully!")

print("\nCreated features:")
print("- overall_score")
print("- attendance_risk")
print("- assignment_risk")
print("- exam_risk")
print("- performance_trend")
print("- declining_performance")
print("- risk_factor_count")

print("\nSample output:")
print(df.head())

print(f"\nSaved to: {OUTPUT_FILE}")