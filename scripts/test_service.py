from dotenv import load_dotenv
from openai import OpenAI

from triage.models import TicketInput
from triage.service import triage_ticket

load_dotenv()

client = OpenAI()

ticket = TicketInput(
    subject="Duplicate charge",
    body="I was charged twice for my subscription and I need a refund.",
)

result = triage_ticket(ticket, client)

print(result)
