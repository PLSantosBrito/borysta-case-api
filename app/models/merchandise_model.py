from pydantic import BaseModel
from datetime import datetime

class MerchandisePIN(BaseModel):
    pin_id: str
    company_name: str
    merchandise_value: float
    origin_state: str
    destination_state: str
    has_previous_infractions: bool

class MerchandiseRiskResponse(BaseModel):
    pin_id: str
    risk_score: int
    recommended_channel: str
    analysis_timestamp: datetime

