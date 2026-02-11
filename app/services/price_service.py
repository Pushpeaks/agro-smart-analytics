import joblib
import numpy as np
import os

# Use a safe path to avoid FileNotFoundError
MODEL_PATH = os.path.join("app", "models", "price_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"CRITICAL: Could not load Price Model: {e}")
    model = None

def predict_price(data):
    if model is None:
        return 0.0

    # RIGHT: Manually map the 4 features in the exact order the model expects
    # Based on your FarmerReportInput, these are the 4 Price features:
    features = [
        data.get("month", 1),
        data.get("last_price", 0.0),
        data.get("rainfall", 0.0),
        data.get("demand_index", 0.0)
    ]

    # Convert to 2D NumPy array (1 row, 4 columns)
    # This replaces the need for separate .reshape() if handled inside the array brackets
    arr = np.array([features]) 
    
    # Predict and return
    pred = model.predict(arr)[0]
    return round(float(pred), 2)