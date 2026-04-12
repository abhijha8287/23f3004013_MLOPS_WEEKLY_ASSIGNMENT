import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load original dataset
df = pd.read_csv("iris.csv")

# Simulate production drift
df_drift = df.copy()

# Shift feature (simulate real-world change)
df_drift["petal_length"] = df_drift["petal_length"] + 1.5

# -------- Plot comparison --------
plt.figure(figsize=(8,5))

sns.kdeplot(df["petal_length"], label="Original", fill=True)
sns.kdeplot(df_drift["petal_length"], label="Drifted", fill=True)

plt.title("Data Drift Detection (Petal Length)")
plt.xlabel("Petal Length")
plt.ylabel("Density")

plt.legend()

# Save plot
plt.savefig("drift_plot.png")
plt.close()

print("Drift plot saved as drift_plot.png")
