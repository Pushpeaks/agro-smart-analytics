import numpy as np
from app.utils.model_loader import load_model

# Load the model once when the server starts
model = load_model("profit_model.pkl")

def predict_profit(data):
    if model is None:
        return 0.0

    # 1. Manually map the 7 features in the exact order of training
    # This prevents the "AttributeError: 'dict' object has no attribute 'area'"
    features = [
        data.get("area", 0.0),
        data.get("rainfall", 0.0),
        data.get("temperature", 0.0),
        data.get("fertilizer_cost", 0.0),
        data.get("previous_yield", 0.0),
        data.get("previous_profit", 0.0),
        data.get("current_cost", 0.0)
    ]

    # 2. Convert to a 2D NumPy array (1 row, 7 columns)
    # This addresses the reshaping issue required by Scikit-learn
    input_array = np.array([features]) 
    
    # 3. Execute prediction
    prediction = model.predict(input_array)[0]
    
    return round(float(prediction), 2)