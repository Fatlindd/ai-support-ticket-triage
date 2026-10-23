from unittest.mock import Mock

import pytest
from openai import APIConnectionError, AuthenticationError

from triage.errors import TriageConfigurationError, TriageUnavailableError
from triage.models import TicketInput
from triage.service import triage_ticket

ticket = TicketInput(subject="Duplicate charge", body="I need a refund.")


def test_api_connection_error_becomes_triage_unavailable_error():
    client = Mock()
    client.responses.parse.side_effect = APIConnectionError(request=Mock())

    with pytest.raises(TriageUnavailableError):
        triage_ticket(ticket, client)


def test_authentication_error_becomes_triage_configuration_error():
    client = Mock()
    client.responses.parse.side_effect = AuthenticationError(
        "invalid",
        response=Mock(),
        body=None,
    )

    with pytest.raises(TriageConfigurationError):
        triage_ticket(ticket, client)
