import json

from dotenv import load_dotenv
from openai import OpenAI

from triage.models import TicketInput
from triage.service import triage_ticket

load_dotenv()

client = OpenAI()

total_cases = 0
fully_correct_cases = 0
correct_intent = 0
correct_department = 0
correct_priority = 0
correct_sentiment = 0

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

        intent_match = result.intent == case["expected_intent"]
        department_match = result.department == case["expected_department"]
        priority_match = result.priority == case["expected_priority"]
        sentiment_match = result.sentiment == case["expected_sentiment"]

        total_cases += 1
        correct_intent += intent_match
        correct_department += department_match
        correct_priority += priority_match
        correct_sentiment += sentiment_match

        if intent_match and department_match and priority_match and sentiment_match:
            fully_correct_cases += 1
            print("PASS")
        else:
            print("FAIL")

        print("---")

print(f"overall case accuracy: {fully_correct_cases / total_cases * 100:.1f}%")
print(f"intent accuracy: {correct_intent / total_cases * 100:.1f}%")
print(f"department accuracy: {correct_department / total_cases * 100:.1f}%")
print(f"priority accuracy: {correct_priority / total_cases * 100:.1f}%")
print(f"sentiment accuracy: {correct_sentiment / total_cases * 100:.1f}%")
