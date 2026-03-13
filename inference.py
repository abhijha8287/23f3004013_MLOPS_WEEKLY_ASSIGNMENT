import mlflow
import mlflow.pyfunc
import pandas as pd

print("Starting inference pipeline...")

# ---------- SET MLFLOW TRACKING LOCATION ----------
mlflow.set_tracking_uri("sqlite:///mlruns/mlflow.db")

# ---------- LOAD MODEL FROM MLFLOW REGISTRY ----------
print("Loading model from MLflow Model Registry...")

model = mlflow.pyfunc.load_model("models:/iris_classifier/latest")

print("Model loaded successfully!")

# ---------- LOAD DATA ----------
df = pd.read_csv("iris.csv")

X = df.drop("species", axis=1)

# ---------- RUN PREDICTIONS ----------
preds = model.predict(X.head(5))

print("Predictions on sample data:")
print(preds)

print("Inference pipeline completed.")