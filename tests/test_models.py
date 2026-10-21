import pytest
from pydantic import ValidationError

from triage.models import TicketTriageResult


def test_valid_triage_result_is_created():
    result = TicketTriageResult(
        intent="billing_issue",
        department="billing",
        priority="high",
        sentiment="negative",
        summary="Customer wants a refund for a duplicate charge.",
    )

    assert result.priority == "high"
    assert result.summary == "Customer wants a refund for a duplicate charge."


def test_invalid_priority_raises_validation_error():
    with pytest.raises(ValidationError):
        TicketTriageResult(
            intent="billing_issue",
            department="billing",
            priority="super_high",
            sentiment="negative",
            summary="Customer wants a refund for a duplicate charge.",
        )
