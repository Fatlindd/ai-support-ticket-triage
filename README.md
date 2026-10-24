# AI Support Ticket Triage API

## Overview

This API classifies a customer support ticket with a large language model. A `POST /triage` request returns the ticket's intent, department, priority, sentiment, and summary, along with token usage for that call.

## Key Features

- Structured LLM outputs
- Pydantic validation
- Support-ticket taxonomy
- FastAPI HTTP API
- Error translation
- Token tracking
- Automated tests
- Evaluation dataset and metrics

## Architecture

```text
Client
  ↓
FastAPI / POST /triage
  ↓
triage_ticket()
  ↓
OpenAI Responses API
  ↓
Structured Pydantic result
```

The service asks the OpenAI Responses API for a structured result and validates it with Pydantic before returning it.

Errors move outward in one direction:

```text
OpenAI SDK errors → application errors → HTTP errors
```

Timeouts, connection failures, and rate limits become an unavailable-service error and an HTTP 503. Authentication and permission failures become a configuration error and an HTTP 500.

## Tech Stack

- Python
- OpenAI Responses API
- Pydantic
- FastAPI
- Uvicorn
- pytest
- python-dotenv

## Project Structure

- `src/triage/` contains the domain models, prompt, triage service, HTTP API, and application errors.
- `tests/` contains unit and API tests. Tests isolate external OpenAI behavior with mocks where appropriate.
- `evals/` contains the curated evaluation cases and the script that scores them.
- `docs/` contains the support-ticket taxonomy.
- `scripts/` contains small manual scripts for checking the API connection and sample tickets.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`.

## Run the API

From the project root:

```bash
PYTHONPATH=src uvicorn triage.api:app --reload
```

Interactive API docs are available at http://127.0.0.1:8000/docs.

## Example POST /triage request

```json
{
  "subject": "Account locked",
  "body": "My account is locked and I cannot sign in."
}
```

## Example response

The fields below match the API schema. The summary and token counts are examples, not a fixed result.

```json
{
  "result": {
    "intent": "account_access",
    "department": "accounts",
    "priority": "urgent",
    "sentiment": "negative",
    "summary": "The customer's account is locked and they cannot sign in."
  },
  "input_tokens": 420,
  "output_tokens": 48,
  "total_tokens": 468
}
```

## Tests

```bash
PYTHONPATH=src pytest -v
```

## Evals

```bash
PYTHONPATH=src python evals/run_evals.py
```

The evaluation dataset contains 10 curated cases. The printed accuracies measure performance on that dataset. They are not a guarantee of production accuracy.

## Domain Taxonomy

Allowed intents, departments, priorities, sentiments, and summary rules are defined in `docs/domain.md`.

## What This Project Demonstrates

This is a small Applied AI Engineering project. It shows structured outputs, validation, prompt design, reliability, evals, API design, error boundaries, and separation of concerns. It is a learning project with a small evaluation set, not a production support system.
