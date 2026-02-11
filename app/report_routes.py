from app.services.profit_service import predict_profit
from app.services.yield_service import predict_yield
from app.services.price_service import predict_price


def generate_report(data: dict):
    profit_input = [
        data["area"],
        data["rainfall"],
        data["temperature"],
        data["fertilizer_cost"],
        data["previous_yield"],
        data["previous_profit"],
        data["current_cost"],
    ]

    yield_input = [
        data["area"],
        data["rainfall"],
        data["temperature"],
        data["fertilizer"],
        data["irrigation"],
    ]

    price_input = [
        data["month"],
        data["last_price"],
        data["rainfall"],
        data["demand_index"],
    ]

    profit = predict_profit(profit_input)
    yield_pred = predict_yield(yield_input)
    price = predict_price(price_input)

    # ---------- simple logic (recommendation engine) ----------

    advice = []
    risk = "Low"

    if profit < 0:
        advice.append("Loss expected. Reduce costs or avoid planting this season.")
        risk = "High"

    if yield_pred < 15:
        advice.append("Low yield predicted. Improve irrigation and fertilizer usage.")

    if price < data["last_price"]:
        advice.append("Market price may drop. Consider delaying selling.")

    if price > data["last_price"]:
        advice.append("Price may increase. Good time to sell later.")

    if not advice:
        advice.append("Conditions look good. Proceed with cultivation.")

    return {
        "expected_yield": yield_pred,
        "expected_price": price,
        "expected_profit": profit,
        "risk_level": risk,
        "advice": advice,
    }