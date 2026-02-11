from fastapi import APIRouter
from app.schemas import FarmerReportInput
from app.services.report_service import generate_report

router = APIRouter()


@router.post("/farmer-report")
def farmer_report(data: FarmerReportInput):
    result = generate_report(data)
    return result