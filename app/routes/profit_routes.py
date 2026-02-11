from fastapi import APIRouter
from app.schemas import ProfitInput
from app.services.profit_service import predict_profit

router = APIRouter()


@router.post("/profit")
def profit(data: ProfitInput):
    result = predict_profit(data.dict())
    return {"predicted_profit": result}