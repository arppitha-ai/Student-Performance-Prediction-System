import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    "student_id": range(1, n+1),
    "gender": np.random.choice(["M","F"], n),
    "school_type": np.random.choice(["Govt","Private"], n),
    "prior_gpa": np.random.uniform(2, 10, n),
    "attendance_pct": np.random.uniform(50, 100, n),
    "quiz_avg": np.random.uniform(20, 100, n),
    "assign_avg": np.random.uniform(20, 100, n),
    "midterm": np.random.uniform(20, 100, n),
    "study_hours_wk": np.random.uniform(0, 20, n),
}

df = pd.DataFrame(data)

# Create target (REALISTIC RULE)
df["final_score"] = (
    0.2*df["prior_gpa"] +
    0.2*df["attendance_pct"] +
    0.2*df["quiz_avg"] +
    0.2*df["assign_avg"] +
    0.2*df["midterm"]
)

df["passed"] = (df["final_score"] > 50).astype(int)

df.to_csv("data/students.csv", index=False)

print("Dataset created!")
