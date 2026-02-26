from feast import FeatureStore
import joblib
import pandas as pd

# Initialize Feast store
store = FeatureStore(repo_path=".")

# Load trained model
model = joblib.load("feast_model.pkl")

# Simulate real-time entity requests
entity_rows = [
    {"iris_id": 1},
    {"iris_id": 2},
    {"iris_id": 3},
]

# Fetch features from online store
online_features = store.get_online_features(
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
    ],
    entity_rows=entity_rows,
).to_dict()

# Convert to DataFrame
features_df = pd.DataFrame(online_features)
X = features_df[[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]]

# Predict
predictions = model.predict(X)

print("Online features retrieved:")
print(features_df)

print("\nPredictions:")
print(predictions)
