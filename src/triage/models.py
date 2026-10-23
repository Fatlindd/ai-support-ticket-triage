from enum import StrEnum

from pydantic import BaseModel


class Intent(StrEnum):
    BILLING_ISSUE = "billing_issue"
    TECHNICAL_ISSUE = "technical_issue"
    ACCOUNT_ACCESS = "account_access"
    SUBSCRIPTION_CHANGE = "subscription_change"
    PRODUCT_QUESTION = "product_question"
    COMPLAINT = "complaint"
    GENERAL_INQUIRY = "general_inquiry"


class Department(StrEnum):
    BILLING = "billing"
    TECHNICAL_SUPPORT = "technical_support"
    ACCOUNTS = "accounts"
    CUSTOMER_CARE = "customer_care"


class Priority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Sentiment(StrEnum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class TicketInput(BaseModel):
    subject: str
    body: str


class TicketTriageResult(BaseModel):
    intent: Intent
    department: Department
    priority: Priority
    sentiment: Sentiment
    summary: str


class TriageRunResult(BaseModel):
    result: TicketTriageResult
    input_tokens: int
    output_tokens: int
    total_tokens: int
