import pandas as pd

# Allowed outputs
valid_labels = ["setosa", "versicolor", "virginica"]

df = pd.read_csv("test.csv")

correct = 0
format_correct = 0

total = len(df)

print("Start testing manually in playground...\n")

for i, row in df.iterrows():
    input_text_v1 = f"sepal_length: {row['sepal_length']}, sepal_width: {row['sepal_width']}, petal_length: {row['petal_length']}, petal_width: {row['petal_width']}"
    
    input_text_v2 = f"A flower has sepal length {row['sepal_length']} cm, sepal width {row['sepal_width']} cm, petal length {row['petal_length']} cm, and petal width {row['petal_width']} cm. Identify the species."

    print(f"\nSample {i+1}")
    print("Actual:", row["species"])
    print("Input v1:", input_text_v1)
    print("Input v2:", input_text_v2)

    pred = input("Enter model prediction: ").strip().lower()

    # Accuracy check
    if pred == row["species"]:
        correct += 1

    # Format compliance check
    if pred in valid_labels:
        format_correct += 1

accuracy = correct / total
format_compliance = format_correct / total

print("\n----- FINAL RESULTS -----")
print("Accuracy:", accuracy)
print("Format Compliance:", format_compliance)
