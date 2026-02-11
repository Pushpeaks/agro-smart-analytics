import pandas as pd
import numpy as np
import os
import random

os.makedirs("ml/datasets", exist_ok=True)

np.random.seed(42)

N = 3000   # number of samples


# ==============================
# PROFIT DATASET
# ==============================
area = np.random.uniform(1, 5, N)
rainfall = np.random.uniform(50, 200, N)
temp = np.random.uniform(20, 40, N)
fert_cost = np.random.uniform(2000, 8000, N)
prev_yield = area * rainfall * 0.1 + np.random.normal(0, 5, N)
prev_profit = prev_yield * 1200
current_cost = fert_cost + np.random.uniform(1000, 4000, N)

profit = (prev_yield * 1500) - current_cost + np.random.normal(0, 2000, N)

profit_df = pd.DataFrame({
    "area": area,
    "rainfall": rainfall,
    "temperature": temp,
    "fertilizer_cost": fert_cost,
    "previous_yield": prev_yield,
    "previous_profit": prev_profit,
    "current_cost": current_cost,
    "profit": profit
})

profit_df.to_csv("ml/datasets/profit_data.csv", index=False)



# ==============================
# YIELD DATASET
# ==============================
fertilizer = np.random.uniform(50, 200, N)
irrigation = np.random.uniform(1, 10, N)

yield_val = area * fertilizer * 0.3 + rainfall * 0.2 + np.random.normal(0, 10, N)

yield_df = pd.DataFrame({
    "area": area,
    "rainfall": rainfall,
    "temperature": temp,
    "fertilizer": fertilizer,
    "irrigation": irrigation,
    "yield": yield_val
})

yield_df.to_csv("ml/datasets/yield_data.csv", index=False)



# ==============================
# PRICE DATASET
# ==============================
month = np.random.randint(1, 13, N)
last_price = np.random.uniform(10, 60, N)
demand = np.random.uniform(1, 5, N)

price = last_price + demand*3 - rainfall*0.01 + np.random.normal(0, 2, N)

price_df = pd.DataFrame({
    "month": month,
    "last_price": last_price,
    "rainfall": rainfall,
    "demand_index": demand,
    "price": price
})

price_df.to_csv("ml/datasets/price_data.csv", index=False)


# ==============================
# CROP RECOMMENDATION DATASET
# ==============================
crops = ["Rice", "Wheat", "Cotton", "Maize", "Sugarcane"]
crop_data = []

for i in range(N):
    r = rainfall[i]
    t = temp[i]
    f = fertilizer[i]
    a = area[i]
    
    # Simple logic to determine "best" crop
    if r > 160: crop = "Rice"
    elif t > 35: crop = "Cotton"
    elif f > 150: crop = "Sugarcane"
    elif t < 25: crop = "Wheat"
    else: crop = "Maize"
    
    crop_data.append([a, r, t, f, crop])

crop_df = pd.DataFrame(crop_data, columns=["area", "rainfall", "temperature", "fertilizer", "crop"])
crop_df.to_csv("ml/datasets/crop_data.csv", index=False)

print("✅ All datasets generated inside ml/datasets/")