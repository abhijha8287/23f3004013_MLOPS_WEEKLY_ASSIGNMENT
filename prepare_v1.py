import pandas as pd
import json

df = pd.read_csv("iris.csv")

with open("iris_v1.jsonl", "w") as f:
    for _, row in df.iterrows():
        record = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{
                        "text": f"sepal_length: {row.iloc[0]}, sepal_width: {row.iloc[1]}, petal_length: {row.iloc[2]}, petal_width: {row.iloc[3]}"
                    }]
                },
                {
                    "role": "model",
                    "parts": [{
                        "text": row.iloc[4]
                    }]
                }
            ]
        }
        f.write(json.dumps(record) + "\n")

print("v1 fixed JSONL created")