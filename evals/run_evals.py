import json

from dotenv import load_dotenv
from openai import OpenAI

from triage.models import TicketInput
from triage.service import triage_ticket

load_dotenv()

client = OpenAI()

with open("evals/cases.jsonl") as cases_file:
    for line in cases_file:
        line = line.strip()
        if not line:
            continue

        case = json.loads(line)
        ticket = TicketInput(subject=case["subject"], body=case["body"])
        run = triage_ticket(ticket, client)
        result = run.result

        print(case["subject"])
        print(
            case["expected_intent"],
            case["expected_department"],
            case["expected_priority"],
            case["expected_sentiment"],
        )
        print(result.intent, result.department, result.priority, result.sentiment)

        if (
            result.intent == case["expected_intent"]
            and result.department == case["expected_department"]
            and result.priority == case["expected_priority"]
            and result.sentiment == case["expected_sentiment"]
        ):
            print("PASS")
        else:
            print("FAIL")

        print("---")
