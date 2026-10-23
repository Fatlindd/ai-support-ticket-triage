from openai import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    PermissionDeniedError,
    RateLimitError,
)

from triage.errors import TriageConfigurationError, TriageUnavailableError
from triage.models import TicketInput, TicketTriageResult, TriageRunResult
from triage.prompts import TRIAGE_SYSTEM_PROMPT


def triage_ticket(ticket: TicketInput, client: OpenAI) -> TriageRunResult:
    try:
        response = client.responses.parse(
            model="gpt-4.1-mini",
            instructions=TRIAGE_SYSTEM_PROMPT,
            input=f"Subject: {ticket.subject}\n\n{ticket.body}",
            text_format=TicketTriageResult,
        )
    except (APITimeoutError, APIConnectionError, RateLimitError) as exc:
        raise TriageUnavailableError("OpenAI is temporarily unavailable.") from exc
    except (AuthenticationError, PermissionDeniedError) as exc:
        raise TriageConfigurationError("OpenAI client configuration is invalid.") from exc

    if response.output_parsed is None:
        raise ValueError("Model response did not include a parsed triage result.")

    return TriageRunResult(
        result=response.output_parsed,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        total_tokens=response.usage.total_tokens,
    )
