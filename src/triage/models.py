from pydantic import BaseModel


class TicketInput(BaseModel):
    subject: str
    body: str


class TicketTriageResult(BaseModel):
    intent: str
    department: str
    priority: str
    sentiment: str
    summary: str
