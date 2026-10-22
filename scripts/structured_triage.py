from dotenv import load_dotenv
from openai import OpenAI

from triage.models import TicketTriageResult
from triage.prompts import TRIAGE_SYSTEM_PROMPT

load_dotenv()

client = OpenAI()

response = client.responses.parse(
    model="gpt-4.1-mini",
    instructions=TRIAGE_SYSTEM_PROMPT,
    input="I was charged twice for my subscription and I need a refund.",
    text_format=TicketTriageResult,
)

print(response.output_parsed)
