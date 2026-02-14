import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime
from google.cloud import storage
import os

BUCKET_NAME = "mlops-week1-23f3004013"
DATA_BLOB = "data/iris.csv"

print("Starting training pipeline...")

# ---------- DOWNLOAD DATA FROM GCS ----------
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

blob = bucket.blob(DATA_BLOB)
blob.download_to_filename("iris.csv")

print("Dataset downloaded from GCS")

# ---------- TRAIN MODEL ----------
df = pd.read_csv("iris.csv")

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Model trained. Accuracy = {acc}")

# ---------- CREATE TIMESTAMP FOLDER ----------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

model_file = f"model.pkl"
metrics_file = f"metrics.txt"

joblib.dump(model, model_file)

with open(metrics_file, "w") as f:
    f.write(f"accuracy={acc}")

# ---------- UPLOAD ARTIFACTS TO GCS ----------
artifact_path = f"artifacts/{timestamp}/"

bucket.blob(artifact_path + model_file).upload_from_filename(model_file)
bucket.blob(artifact_path + metrics_file).upload_from_filename(metrics_file)

print(f"Artifacts stored in GCS at {artifact_path}")
print("Training pipeline completed successfully.")
