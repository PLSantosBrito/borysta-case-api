from app.models.merchandise_model import  MerchandisePIN, MerchandiseRiskResponse
from datetime import datetime

def calculate_risk(data: MerchandisePIN) -> MerchandiseRiskResponse:

    return {
        "pin_id": data.pin_id,
        "risk_score": 80,
        "recommended_channel": "VERDE",
        "analysis_timestamp": datetime.utcnow().isoformat(),
    }