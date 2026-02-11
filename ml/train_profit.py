import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

from sklearn.metrics import r2_score, mean_absolute_error



data = pd.read_csv("datasets/profit_data.csv")

X = data.drop("profit", axis=1)
y = data["profit"]

model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "app/models/profit_model.pkl")

print(" profit_model saved")

