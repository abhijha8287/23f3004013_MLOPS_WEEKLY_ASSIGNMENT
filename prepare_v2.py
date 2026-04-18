import pandas as pd
import json

df = pd.read_csv("iris.csv")

with open("iris_v2.jsonl", "w") as f:
    for _, row in df.iterrows():
        record = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{
                        "text": f"A flower has sepal length {row.iloc[0]} cm, sepal width {row.iloc[1]} cm, petal length {row.iloc[2]} cm, and petal width {row.iloc[3]} cm. Identify the species."
                    }]
                },
                {
                    "role": "model",
                    "parts": [{
                        "text": f"This is Iris {row.iloc[4]}."
                    }]
                }
            ]
        }
        f.write(json.dumps(record) + "\n")

print("v2 fixed JSONL created")