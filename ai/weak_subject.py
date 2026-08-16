import pandas as pd

# Load processed academic dataset
df = pd.read_csv("data/processed_academic_data.csv")

# Subjects to check
subjects = ["Maths", "Python", "DBMS", "Java"]

# Marks below this value are considered weak
WEAK_MARK = 50

print("\nWEAK SUBJECT DETECTION")
print("======================")

for index, row in df.iterrows():

    weak_subjects = []

    for subject in subjects:
        if subject in df.columns:
            if row[subject] < WEAK_MARK:
                weak_subjects.append(subject)

    student_id = row["student_id"] if "student_id" in df.columns else index + 1

    if weak_subjects:
        print(f"Student {student_id}: Weak Subjects → {', '.join(weak_subjects)}")
    else:
        print(f"Student {student_id}: No weak subjects")

print("\nWeak subject detection completed!")