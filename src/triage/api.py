from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI

from triage.errors import TriageConfigurationError, TriageUnavailableError
from triage.models import TicketInput, TriageRunResult
from triage.service import triage_ticket

load_dotenv()

app = FastAPI(title="AI Support Ticket Triage API")


@app.post("/triage", response_model=TriageRunResult)
def triage(ticket: TicketInput) -> TriageRunResult:
    client = OpenAI()
    try:
        return triage_ticket(ticket, client)
    except TriageUnavailableError as exc:
        raise HTTPException(
            status_code=503,
            detail="Triage service is temporarily unavailable.",
        ) from exc
    except TriageConfigurationError as exc:
        raise HTTPException(
            status_code=500,
            detail="Triage service configuration error.",
        ) from exc
