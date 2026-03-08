import joblib
import pandas as pd
from sklearn.metrics import accuracy_score


def test_model_file_exists():

    model = joblib.load("model.pkl")

    assert model is not None


def test_model_accuracy():

    df = pd.read_csv("iris.csv")

    X = df.drop("species", axis=1)
    y = df["species"]

    model = joblib.load("model.pkl")

    preds = model.predict(X)

    accuracy = accuracy_score(y, preds)

    assert accuracy >= 0.80
