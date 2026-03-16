from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class RiskChannel(str, Enum):
    VERMELHO = "VERMELHO"
    AMARELO = "AMARELO"
    VERDE = "VERDE"

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
    recommended_channel: RiskChannel
    analysis_timestamp: datetime

