import pandas as pd
import shap
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("iris.csv")

X = df.iloc[:, :4]
y = df.iloc[:, 4]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# SHAP explainer
explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

# --------- FIX START ---------

# Save overall summary plot (works for both versions)
shap.summary_plot(shap_values, X, show=False)
plt.savefig("shap_summary.png")
plt.close()

print("SHAP summary plot saved as shap_summary.png")

# Handle both SHAP output formats
if isinstance(shap_values, list):
    # Old SHAP → list of arrays
    virginica_shap = shap_values[2]
else:
    # New SHAP → 3D array (samples, features, classes)
    virginica_shap = shap_values[:, :, 2]

# Save Virginica-specific plot
shap.summary_plot(virginica_shap, X, show=False)
plt.savefig("shap_virginica.png")
plt.close()

print("Virginica SHAP plot saved as shap_virginica.png")

# --------- FIX END ---------