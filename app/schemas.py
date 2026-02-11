from pydantic import BaseModel

class ProfitInput(BaseModel):
    area: float
    rainfall: float
    temperature: float
    fertilizer_cost: float
    previous_yield: float
    previous_profit: float
    current_cost: float

class YieldInput(BaseModel):
    # Note: area, rainfall, and temperature are already in ProfitInput
    # We will handle the overlap in the combined class
    fertilizer: float
    irrigation: float

class PriceInput(BaseModel):
    month: int
    last_price: float
    demand_index: float

# This inherits all fields automatically
class FarmerReportInput(ProfitInput, YieldInput, PriceInput):
    """
    Combines all fields. Pydantic is smart enough to merge 
    duplicate fields (like rainfall) into one requirement.
    """
    pass