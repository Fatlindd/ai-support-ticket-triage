# Support Ticket Triage Domain

This document defines the labels an AI system may assign when classifying a customer support ticket. Each ticket receives one intent, one department, one priority, one sentiment, and a short summary.

## Intent

Intent is the customer's main problem or request. Choose the single category that best matches what the customer wants done. If a ticket could fit more than one category, use the specific operational request (billing, access, subscription, or a broken product) rather than the customer's tone.

### billing_issue

The customer is asking about a charge, invoice, payment failure, or refund. This includes duplicate charges, unexpected fees, and requests to return money already paid.

### technical_issue

Something in the product is broken, erroring, or unavailable. The customer wants the failure investigated or fixed. Questions about how a working feature is supposed to behave belong under `product_question`.

### account_access

The customer cannot get into the account or needs help with identity checks. This includes forgotten passwords, locked accounts, failed login, and two-factor or email verification problems.

### subscription_change

The customer wants to change an existing plan. This includes upgrades, downgrades, cancellations, pauses, and renewals. Questions only about a charge or a refund of a past payment belong under `billing_issue`.

### product_question

The customer wants to understand a feature, a limit, or how to complete a task in the product. The product is not reported as broken. Requests to build something that does not exist are still product questions when the customer is asking what the product can do.

### complaint

The customer's main request is to report a bad experience, poor service, or unmet expectation, and to have that dissatisfaction acknowledged or escalated. If they also ask for a refund, a fix, access help, or a plan change, classify the ticket by that operational request instead.

### general_inquiry

The customer asks a question that is not about billing, a broken product, account access, a plan change, or how to use a feature. Typical cases are business hours, contact options, and company information.

## Department

Department is the team that should own the ticket. It is not the same as intent: intent describes the request, and department describes who handles it.

### billing

Owns money and commercial plan changes. Handles `billing_issue` and `subscription_change` tickets, including invoices, failed payments, refunds, and plan upgrades, downgrades, or cancellations.

### technical_support

Owns product behavior. Handles `technical_issue` and `product_question` tickets, including errors, outages, and questions about how a feature works.

### accounts

Owns identity and sign-in. Handles `account_access` tickets, including password resets, locked accounts, and verification problems.

### customer_care

Owns experience and non-product questions. Handles `complaint` and `general_inquiry` tickets, including service feedback and general company questions.

## Priority

Priority reflects business impact, urgency, blocked access or security risk, and time sensitivity.

- **low**: The request has little impact and no deadline, so it can wait in the normal queue.
- **medium**: The customer is affected, but they can keep working or the request can follow the standard response time.
- **high**: The request has significant business or financial impact, or it blocks important work.
- **urgent**: The ticket needs immediate attention because of a security risk, a full account lockout, a widespread outage, data loss, or a deadline that cannot slip.

## Sentiment

Sentiment describes the customer's tone in the ticket.

- **positive**: The customer is pleased, grateful, or complimentary.
- **neutral**: The customer states a request or facts without strong emotion.
- **negative**: The customer is frustrated, angry, disappointed, or dissatisfied.

## Summary Rules

1. Write one or two sentences that state what the customer wants and the key facts given in the ticket.
2. Include only information that appears in the ticket. Do not invent amounts, dates, causes, account details, or outcomes.
3. Leave out greetings and signatures. Keep emotional wording only when it is needed to reflect a complaint.
