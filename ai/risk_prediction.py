import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


# Load processed dataset
df = pd.read_csv("data/processed_academic_data.csv")

# Create risk label
def get_risk(row):
    if row["overall_score"] < 50 or row["attendance_percentage"] < 65:
        return 1
    return 0


df["at_risk"] = df.apply(get_risk, axis=1)

# Features
features = [
    "attendance_percentage",
    "assignment_average",
    "assignment_completion",
    "exam_average",
    "previous_performance",
    "recent_performance",
    "performance_trend"
]

X = df[features]
y = df["at_risk"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Models
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression())
    ]),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
}

results = {}

# Train and evaluate
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

    print("\n", name)
    print("-------------------------")
    print("Accuracy :", round(accuracy, 3))
    print("Precision:", round(precision, 3))
    print("Recall   :", round(recall, 3))
    print("F1 Score :", round(f1, 3))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))


# Display comparison
print("\nMODEL COMPARISON")
print("============================")

for name, metrics in results.items():
    print(
        name,
        "Accuracy:", round(metrics["Accuracy"], 3),
        "Precision:", round(metrics["Precision"], 3),
        "Recall:", round(metrics["Recall"], 3),
        "F1:", round(metrics["F1 Score"], 3)
    )


# Train final model
final_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

final_model.fit(X_train, y_train)

# Save model
joblib.dump(final_model, "models/risk_model.pkl")

print("\nRisk model saved successfully!")