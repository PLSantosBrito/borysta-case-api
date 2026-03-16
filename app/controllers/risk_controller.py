from typing import Union, List
from app.models.merchandise_model import MerchandisePIN
from app.services.risk_service import calculate_risk

def process_risk(data: Union[MerchandisePIN, List[MerchandisePIN]]):

    if isinstance(data, list):
        return [calculate_risk(item) for item in data]

    return calculate_risk(data)