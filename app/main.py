import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes.profit_routes import router as profit_router
from app.routes.yield_routes import router as yield_router
from app.routes.price_routes import router as price_router
from app.routes.report_routes import router as report_router

app = FastAPI(
    title="Agro AI Backend",
    description="ML-powered agricultural predictions for profit, yield, and price.",
    version="1.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Profit Prediction Routes
app.include_router(
    profit_router, 
    prefix="/predict/profit", 
    tags=["Profit Analysis"]
)

# 2. Yield Prediction Routes
app.include_router(
    yield_router, 
    prefix="/predict/yield", 
    tags=["Yield Analysis"]
)

# 3. Price Prediction Routes
app.include_router(
    price_router, 
    prefix="/predict/price", 
    tags=["Price Trends"]
)

# 4. Comprehensive Farmer Report
app.include_router(
    report_router, 
    prefix="/report", 
    tags=["Farmer Reports"]
)

# Serve Frontend static files for Hugging Face deployment
# The 'build' folder is created during the Docker build process
frontend_path = "agro-frontend/build"
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
    
    # Optional: Catch-all for Client-Side Routing (React Router)
    @app.exception_handler(404)
    async def not_found_handler(request, exc):
        return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/api/status")
async def status():
    return {"message": "Welcome to Agro AI Backend API", "status": "online"}