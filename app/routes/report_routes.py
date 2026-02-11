from fastapi import APIRouter
from app.schemas import FarmerReportInput
from app.services.report_service import generate_report

router = APIRouter()


@router.post("/generate")
def generate_comprehensive_report(data: FarmerReportInput):
    result = generate_report(data)
    return result

