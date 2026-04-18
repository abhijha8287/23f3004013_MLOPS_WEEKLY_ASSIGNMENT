import pandas as pd

df = pd.read_csv("iris.csv")

# Take 20 random samples
test_df = df.sample(20, random_state=42)

test_df.to_csv("test.csv", index=False)

print("Test dataset created")
