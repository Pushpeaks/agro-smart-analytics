from app.services import profit_service, yield_service, price_service, crop_service
from fastapi import HTTPException

def generate_report(data):
    try:
        # 1. Prepare data for Profit model
        profit_data = {
            "area": data.area,
            "rainfall": data.rainfall,
            "temperature": data.temperature,
            "fertilizer_cost": data.fertilizer_cost,
            "previous_yield": data.previous_yield,
            "previous_profit": data.previous_profit,
            "current_cost": data.current_cost
        }
        
        # 2. Prepare data for Yield model
        yield_data = {
            "area": data.area,
            "rainfall": data.rainfall,
            "temperature": data.temperature,
            "fertilizer": data.fertilizer,
            "irrigation": data.irrigation
        }
        
        # 3. Prepare data for Price model
        price_data = {
            "month": data.month,
            "last_price": data.last_price,
            "rainfall": data.rainfall,
            "demand_index": data.demand_index
        }

        # 4. Prepare data for Crop Recommendation (area, rainfall, temperature, fertilizer)
        crop_data = {
            "area": data.area,
            "rainfall": data.rainfall,
            "temperature": data.temperature,
            "fertilizer": data.fertilizer
        }

        # Attempt predictions
        # These call the predict functions in your individual services
        pred_profit = profit_service.predict_profit(profit_data)
        pred_yield = yield_service.predict_yield(yield_data)   
        pred_price = price_service.predict_price(price_data)
        recommended_crop = crop_service.predict_crop(crop_data)

        return {
            "profit": round(float(pred_profit), 2),
            "yield": round(float(pred_yield), 2),
            "price": round(float(pred_price), 2),
            "recommended_crop": recommended_crop,
            "recommendation": "Optimal" if pred_profit > data.current_cost else "High Risk"
        }

    except Exception as e:
        # This will print the exact traceback in your VS Code terminal
        import traceback
        traceback.print_exc() 
        
        # This will tell the frontend exactly what went wrong
        raise HTTPException(status_code=500, detail=f"Service Error: {str(e)}")