from openai import OpenAI

from triage.models import TicketInput, TicketTriageResult
from triage.prompts import TRIAGE_SYSTEM_PROMPT


def triage_ticket(ticket: TicketInput, client: OpenAI) -> TicketTriageResult:
    response = client.responses.parse(
        model="gpt-4.1-mini",
        instructions=TRIAGE_SYSTEM_PROMPT,
        input=f"Subject: {ticket.subject}\n\n{ticket.body}",
        text_format=TicketTriageResult,
    )

    if response.output_parsed is None:
        raise ValueError("Model response did not include a parsed triage result.")

    return response.output_parsed
