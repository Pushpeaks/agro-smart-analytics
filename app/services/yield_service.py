import numpy as np
from app.utils.model_loader import load_model

# Load the model once when the server starts
model = load_model("yield_model.pkl")

def predict_yield(data):
    if model is None:
        return 0.0

    # 1. Manually map the 5 features in the exact order of training (from yield_data.csv)
    # features: area, rainfall, temperature, fertilizer, irrigation
    features = [
        data.get("area", 0.0),
        data.get("rainfall", 0.0),
        data.get("temperature", 0.0),
        data.get("fertilizer", 0.0),
        data.get("irrigation", 0.0)
    ]

    # 2. Convert to a 2D NumPy array
    input_array = np.array([features]) 
    
    # 3. Execute prediction
    prediction = model.predict(input_array)[0]
    
    return round(float(prediction), 2)