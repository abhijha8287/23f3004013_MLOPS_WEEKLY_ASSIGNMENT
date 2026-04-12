import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Step 1: Load dataset
df = pd.read_csv("iris.csv")

# Step 2: Add sensitive attribute
df["location"] = np.random.randint(0, 2, size=len(df))

# Save for reference (optional)
df.to_csv("iris_with_location.csv", index=False)

# Step 3: Define features and target
X = df.iloc[:, :4]      # only original features
y = df.iloc[:, 4]       # species
A = df["location"]      # sensitive attribute

# Step 4: Train-test split (IMPORTANT)
X_train, X_test, y_train, y_test, A_train, A_test = train_test_split(
    X, y, A, test_size=0.2, random_state=42
)

# Step 5: Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)

# Step 7: Fairness metrics
mf = MetricFrame(
    metrics={
        "accuracy": accuracy_score,
        "precision": lambda y_true, y_pred: precision_score(
            y_true, y_pred, average='macro', zero_division=0
        ),
        "recall": lambda y_true, y_pred: recall_score(
            y_true, y_pred, average='macro', zero_division=0
        )
    },
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=A_test
)

# Step 8: Output
print("\nOverall Metrics:")
print(mf.overall)

print("\nMetrics by group:")
print(mf.by_group)