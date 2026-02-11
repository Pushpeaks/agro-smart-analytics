from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import profit_routes, yield_routes, price_routes, report_routes

app = FastAPI(
    title="Agro AI Backend",
    description="ML-powered agricultural predictions for profit, yield, and price.",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Profit Prediction Routes
app.include_router(
    profit_routes.router, 
    prefix="/predict/profit", 
    tags=["Profit Analysis"]
)

# 2. Yield Prediction Routes (Fixed prefix to be specific to yield)
app.include_router(
    yield_routes.router, 
    prefix="/predict/yield", 
    tags=["Yield Analysis"]
)

# 3. Price Prediction Routes (Resolved the AttributeError)
app.include_router(
    price_routes.router, 
    prefix="/predict/price", 
    tags=["Price Trends"]
)

# 4. Comprehensive Farmer Report (Consolidated Logic)
app.include_router(
    report_routes.router, 
    prefix="/report", 
    tags=["Farmer Reports"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to Agro AI Backend API", "status": "online"}