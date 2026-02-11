import joblib
import numpy as np

models = {
    "Profit": "app/models/profit_model.pkl",
    "Yield": "app/models/yield_model.pkl",
    "Price": "app/models/price_model.pkl"
}

for name, path in models.items():
    try:
        model = joblib.load(path)
        # n_features_in_ is a standard attribute for sklearn models
        if hasattr(model, "n_features_in_"):
            print(f"{name} Model expects: {model.n_features_in_} features")
        else:
            print(f"{name} Model: Could not determine feature count automatically.")
    except Exception as e:
        print(f"Error loading {name}: {e}")