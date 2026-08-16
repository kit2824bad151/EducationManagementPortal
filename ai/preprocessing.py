import pandas as pd

# Load dataset
df = pd.read_csv("data/academic_data.csv")

print("Original Data:")
print(df.head())

# Remove duplicate records
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Create performance trend
df["performance_trend"] = (
    df["recent_performance"] -
    df["previous_performance"]
)

print("\nProcessed Data:")
print(df.head())

# Save processed dataset
df.to_csv("data/processed_data.csv", index=False)

print("\nProcessed data saved successfully!")
# Calculate overall academic score
df["overall_score"] = (
    df["assignment_average"] * 0.25 +
    df["exam_average"] * 0.50 +
    df["attendance_percentage"] * 0.15 +
    df["assignment_completion"] * 0.10
)

# Save processed dataset
df.to_csv("data/processed_academic_data.csv", index=False)

print("\nProcessed dataset saved successfully!")