import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib
import os

DATA_PATH = "datasets/yield_data.csv"
MODEL_PATH = "app/models/yield_model.pkl"

os.makedirs("app/models", exist_ok=True)

# =====================
# Load
# =====================
data = pd.read_csv(DATA_PATH)

X = data.drop("yield", axis=1)
y = data["yield"]

# =====================
# Split
# =====================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================
# Train
# =====================
model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Yield R2 Score:", r2_score(y_test, preds))

# =====================
# Save
# =====================
joblib.dump(model, MODEL_PATH)

print("yield_model.pkl saved")