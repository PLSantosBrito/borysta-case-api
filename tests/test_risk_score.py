from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_risk_score_amarelo():
    payload = {
        "pin_id": "123456789",
        "company_name": "Tech Indústria S.A.",
        "merchandise_value": 150000,
        "origin_state": "SP",
        "destination_state": "AM",
        "has_previous_infractions": False
    }

    response = client.post("/api/v1/risk-score", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["recommended_channel"] == "AMARELO"
    assert data["risk_score"] >= 40


def test_risk_score_vermelho():
    payload = {
        "pin_id": "123456789",
        "company_name": "Empresa X",
        "merchandise_value": 600000,
        "origin_state": "SP",
        "destination_state": "AM",
        "has_previous_infractions": False
    }

    response = client.post("/api/v1/risk-score", json=payload)

    data = response.json()

    assert response.status_code == 200
    assert data["recommended_channel"] == "VERMELHO"
    assert data["risk_score"] >= 80

def test_risk_score_verde():
    payload = {
        "pin_id": "123456789",
        "company_name": "Empresa X",
        "merchandise_value": 50000,
        "origin_state": "SP",
        "destination_state": "AM",
        "has_previous_infractions": False
    }

    response = client.post("/api/v1/risk-score", json=payload)

    data = response.json()

    assert response.status_code == 200
    assert data["recommended_channel"] == "VERDE"
    assert data["risk_score"] < 40

def test_invalid_payload():
    payload = {
        "pin_id": "123456789"
    }

    response = client.post("/api/v1/risk-score", json=payload)

    assert response.status_code == 400