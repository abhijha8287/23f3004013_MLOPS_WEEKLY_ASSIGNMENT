from feast import FeatureStore
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Initialize Feast Store
store = FeatureStore(repo_path=".")

# Load entity dataframe (must contain iris_id + event_timestamp)
entity_df = pd.read_parquet("data/iris.parquet")[["iris_id", "event_timestamp"]]

# Fetch historical features from Feast (Offline Store)
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
    ],
).to_df()

# Add target column manually (not stored in feature store)
original_df = pd.read_parquet("data/iris.parquet")
training_df["species"] = original_df["species"]

# Prepare X and y
X = training_df.drop(["iris_id", "event_timestamp", "species"], axis=1)
y = training_df["species"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully using Feast offline features!")

import joblib
joblib.dump(model, "feast_model.pkl")
print("Model saved as feast_model.pkl")