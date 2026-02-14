import joblib
import pandas as pd
from google.cloud import storage

BUCKET_NAME = "mlops-week1-23f3004013"

print("Starting inference pipeline...")

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

# ---------- FIND LATEST MODEL FOLDER ----------
blobs = list(client.list_blobs(BUCKET_NAME, prefix="artifacts/"))

folders = sorted(set([b.name.split("/")[1] for b in blobs if b.name.count("/") > 1]))

latest_folder = folders[-1]
print(f"Using latest model from: {latest_folder}")

# ---------- DOWNLOAD MODEL ----------
model_blob = bucket.blob(f"artifacts/{latest_folder}/model.pkl")
model_blob.download_to_filename("model.pkl")

model = joblib.load("model.pkl")

# ---------- DOWNLOAD DATA ----------
data_blob = bucket.blob("data/iris.csv")
data_blob.download_to_filename("iris.csv")

df = pd.read_csv("iris.csv")
X = df.drop("species", axis=1)

# ---------- RUN PREDICTIONS ----------
preds = model.predict(X.head(5))

print("Predictions on sample data:")
print(preds)

print("Inference pipeline completed.")
