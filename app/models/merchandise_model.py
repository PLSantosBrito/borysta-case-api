from pydantic import BaseModel


class MerchandisePIN(BaseModel):
    pin_id: str


class MerchandiseRiskResponse(BaseModel):
    pin_id: str
    risk_score: int
