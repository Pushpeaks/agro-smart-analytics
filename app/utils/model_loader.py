import joblib
import os

def load_model(model_name):
    # Adjust this path to wherever your .pkl files are stored
    model_path = os.path.join("app", "models", model_name)
    
    if not os.path.exists(model_path):
        print(f"CRITICAL ERROR: Model file not found at {model_path}")
        return None
    
    return joblib.load(model_path)