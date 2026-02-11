import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

# 1. Load dataset
data = pd.read_csv("ml/datasets/crop_data.csv")

# 2. Define features and target
X = data[["area", "rainfall", "temperature", "fertilizer"]]
y = data["crop"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate
accuracy = model.score(X_test, y_test)
print(f"✅ Crop Model trained with accuracy: {accuracy:.2f}")

# 6. Save model
os.makedirs("app/models", exist_ok=True)
with open("app/models/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🚀 model saved as app/models/crop_model.pkl")
