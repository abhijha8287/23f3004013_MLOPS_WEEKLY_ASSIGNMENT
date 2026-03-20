from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(root_path="/proxy/8000")

model = joblib.load("final_model.pkl")

@app.get("/")
def home():
    return {"message": "IRIS API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    preds = model.predict(df)
    return {"prediction": preds.tolist()}