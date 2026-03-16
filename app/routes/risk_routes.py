from fastapi import APIRouter
from typing import Union, List
from app.models.merchandise_model import MerchandisePIN, MerchandiseRiskResponse
from app.controllers.risk_controller import process_risk

router = APIRouter()

@router.post(
    "/risk-score",
    response_model=Union[MerchandiseRiskResponse, List[MerchandiseRiskResponse]],
)
def risk_score(payload: Union[MerchandisePIN, List[MerchandisePIN]]):
    return process_risk(payload)