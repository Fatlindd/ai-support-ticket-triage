from unittest.mock import patch

from fastapi.testclient import TestClient

from triage.api import app
from triage.errors import TriageConfigurationError, TriageUnavailableError
from triage.models import TicketTriageResult, TriageRunResult

client = TestClient(app)

request_body = {
    "subject": "Account locked",
    "body": "My account is locked and I cannot sign in.",
}


def test_successful_triage():
    run = TriageRunResult(
        result=TicketTriageResult(
            intent="account_access",
            department="accounts",
            priority="urgent",
            sentiment="negative",
            summary="The customer's account is locked and they cannot sign in.",
        ),
        input_tokens=10,
        output_tokens=20,
        total_tokens=30,
    )

    with patch("triage.api.triage_ticket", return_value=run):
        response = client.post("/triage", json=request_body)

    assert response.status_code == 200
    body = response.json()["result"]
    assert body["intent"] == "account_access"
    assert body["department"] == "accounts"
    assert body["priority"] == "urgent"


def test_unavailable_service():
    with patch("triage.api.triage_ticket", side_effect=TriageUnavailableError("down")):
        response = client.post("/triage", json=request_body)

    assert response.status_code == 503
    assert response.json()["detail"] == "Triage service is temporarily unavailable."


def test_configuration_error():
    with patch(
        "triage.api.triage_ticket",
        side_effect=TriageConfigurationError("invalid"),
    ):
        response = client.post("/triage", json=request_body)

    assert response.status_code == 500
    assert response.json()["detail"] == "Triage service configuration error."
