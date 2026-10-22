from dotenv import load_dotenv
from openai import OpenAI

from triage.models import TicketInput
from triage.service import triage_ticket

load_dotenv()

client = OpenAI()

tickets = [
    TicketInput(
        subject="Cannot sign in",
        body="I forgot my password and the login page says my account is locked. I cannot access my account.",
    ),
    TicketInput(
        subject="App crashes on launch",
        body="The mobile app closes immediately after I open it. This started today and I cannot use the product.",
    ),
    TicketInput(
        subject="How do I export a report?",
        body="Where do I find the option to export last month's report as a CSV file?",
    ),
    TicketInput(
        subject="Unhelpful support experience",
        body="I waited three days for a reply and the answer did not address my question. I want this poor service reviewed.",
    ),
    TicketInput(
        subject="Office hours",
        body="What are your customer support hours, and which email should I use to reach the company?",
    ),
]

for ticket in tickets:
    print(ticket.subject)
    result = triage_ticket(ticket, client)
    print(result.intent)
    print(result.department)
    print(result.priority)
    print(result.sentiment)
    print(result.summary)
    print("---")
