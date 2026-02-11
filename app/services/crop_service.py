import numpy as np
from app.utils.model_loader import load_model

# Load the model once when the server starts
model = load_model("crop_model.pkl")

def predict_crop(data):
    if model is None:
        return "Unknown"

    # 1. Map features: area, rainfall, temperature, fertilizer
    features = [
        data.get("area", 0.0),
        data.get("rainfall", 0.0),
        data.get("temperature", 0.0),
        data.get("fertilizer", 0.0)
    ]

    # 2. Convert to 2D array
    input_array = np.array([features]) 
    
    # 3. Execute prediction
    prediction = model.predict(input_array)[0]
    
    return str(prediction)
