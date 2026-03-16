import random
from app.models.merchandise_model import  RiskChannel, MerchandisePIN, MerchandiseRiskResponse
from datetime import datetime


def red_channel_rule(data: MerchandisePIN) -> RiskChannel | None:
    if data.has_previous_infractions or data.merchandise_value > 500000:
        return RiskChannel.VERMELHO
    
def yellow_channel_rule(data: MerchandisePIN) -> RiskChannel | None:
    if 100000 <= data.merchandise_value <= 500000:
        return RiskChannel.AMARELO
    
def green_channel_rule(data: MerchandisePIN) -> RiskChannel | None :
    return RiskChannel.VERDE


def generate_score(channel: RiskChannel) -> int:
    ranges = {"VERMELHO": (80, 100), "AMARELO": (40, 79), "VERDE": (0, 39)}

    min_score, max_score = ranges[channel]
    return random.randint(min_score, max_score)


def calculate_risk(data: MerchandisePIN) -> MerchandiseRiskResponse:

    rules = [red_channel_rule, yellow_channel_rule]
    
    for rule in rules:
        channel = rule(data)
        if channel:
            score = generate_score(channel)
            return {
                "pin_id": data.pin_id,
                "risk_score": score,
                "recommended_channel": channel,
                "analysis_timestamp": datetime.utcnow().isoformat(),
            }

    channel = green_channel_rule(data)
    score = generate_score(channel)

    return {
        "pin_id": data.pin_id,
        "risk_score": score,
        "recommended_channel": channel,
        "analysis_timestamp": datetime.utcnow().isoformat(),
    }