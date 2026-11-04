# Fernledger: Company Brief

> **Fictional company.** Fernledger, its customers, numbers and events are invented for a portfolio project. All data in this repo is synthetic. Any resemblance to a real company is unintended.

## 1. The company in one line

**Fernledger is invoicing and get-paid software for small businesses and freelancers.** Customers create and send invoices, their clients pay by card or bank transfer through a link, and the money lands in the customer's bank. Fernledger syncs everything to their accounting software and handles sales tax and VAT on invoices.

Think: Stripe invoicing + FreshBooks, built for one-person businesses and small teams.

| Fact | Value |
|---|---|
| Founded | 2019 |
| Headquarters | Austin, Texas, USA (remote-first; UK office in Manchester) |
| Markets | United States, United Kingdom, Canada |
| Employees | about 140 |
| Customers | about 6,500 businesses in Apr 2025, growing to about 10,000 by Sep 2026 |
| Business model | Monthly subscription (SaaS) + a small fee on each card payment |
| Apps | Web app, iOS app, Android app |

## 2. Who the customers are

| Business type | Share | Example |
|---|---|---|
| Freelancers and solo consultants | 45% | Designer, copywriter, developer, photographer |
| Small agencies (2 to 15 people) | 25% | Marketing agency, web studio |
| Trades and home services | 18% | Plumber, electrician, cleaner |
| Small product and retail businesses | 12% | Bakery doing catering orders, boutique doing wholesale |

Country split: US 60%, UK 25%, Canada 15%. Currencies: USD, GBP, CAD.

## 3. Plans and prices

| Plan | Price (until 30 Jun 2026) | Price (from 1 Jul 2026) | Card fee | Limits | Share of customers |
|---|---|---|---|---|---|
| Free | $0 | $0 | 2.9% + 30c | 5 invoices a month, 1 user | 45% |
| Starter | $15/month | **$19/month** | 2.9% + 30c | Unlimited invoices, recurring invoices, 1 user | 30% |
| Pro | $35/month | **$39/month** | 2.7% + 30c | + QuickBooks/Xero sync, late fees, 3 users | 18% |
| Business | $79/month | $79/month | 2.5% + 30c | + multi-currency, priority support, 10 users | 7% |

Annual billing gets 2 months free. Free customers often upgrade to Starter when they hit the 5-invoice limit.

## 4. Product features (what tickets are about)

- **Invoices:** create, send by email or link, PDF download, templates, logo and branding
- **Recurring invoices:** bill a client automatically every week or month
- **Reminders and late fees:** automatic chasers for overdue invoices
- **Get paid:** clients pay by card or bank transfer (ACH in US, BACS in UK); money is deposited to the customer's bank in 2 business days
- **Tax:** sales tax (US), VAT (UK), GST/HST (Canada) on invoices; tax summary reports
- **Integrations:** QuickBooks Online, Xero, Zapier, Google Calendar (for time tracking), bank feeds
- **Team:** invite users, roles and permissions (Pro and Business)
- **Mobile apps:** send invoices and see payments on the go

Payment processing runs through a third-party payment processor behind the scenes.

## 5. The support team

| Item | Detail |
|---|---|
| Channels | Email (50%), live chat (35%), in-app web form (15%) |
| Hours | Chat: Mon to Fri, 7am to 11pm US Eastern. Email and web form: 24/7, answered Mon to Fri plus a small weekend shift |
| Team size | 22 agents: 14 Tier 1 (general), 6 Tier 2 (payments and billing specialists), 2 team leads. Tier 3 = engineering escalations |
| AI assistant | **"Fern Assist"**, launched 4 Aug 2025 on chat and the web form (see events) |
| Help centre | About 180 articles |
| Helpdesk tool | Exports tickets as CSV (this is the data we analyse) |

**First-response targets by plan (SLA):**

| Plan | Target first response |
|---|---|
| Business | 1 hour |
| Pro | 4 hours |
| Starter | 12 hours |
| Free | 24 hours |

## 6. Ticket categories

The "true" category of each ticket. The helpdesk export does **not** contain this cleanly (agents' tags are messy and often missing), which is why we classify the text with AI and check it against an answer key.

| Category | Baseline share | Sub-topics |
|---|---|---|
| Invoicing | 22% | Creating/sending, recurring invoices, reminders, late fees, templates, client didn't receive invoice |
| Client payments | 18% | Client's card declined, payment pending, deposit not arrived, dispute/chargeback, bank transfer issues |
| Billing and subscription | 14% | Plan change, charged twice, refund request, price questions, cancel/downgrade |
| Integrations | 13% | QuickBooks sync, Xero sync, Zapier, bank feed disconnected |
| Account and access | 12% | Login, two-factor codes, adding team members, permissions |
| Bugs and performance | 9% | Mobile app crash, PDF won't generate, slow loading, error messages |
| Tax and compliance | 7% | Adding VAT/sales tax, tax rates, tax reports |
| Feature requests and feedback | 5% | "Can you add...", general feedback |

## 7. Events timeline (what the analysis should uncover)

| Date | Event | Effect on tickets |
|---|---|---|
| 15 Apr 2025, 31 Jan 2026, 15 Apr 2026 | Tax deadlines (US 15 Apr, UK 31 Jan) | Tax tickets up about 80% in the 3 weeks before each |
| 9 Jun 2025 | QuickBooks sync update ships with a bug | Integration tickets about 3x for 3 weeks; many reopens |
| **4 Aug 2025** | **Fern Assist AI launches** on chat and web form | Bot handles about 45% of chat/web-form tickets. Resolves most how-to questions, but fails on payments and billing: high escalation, more reopens, lower satisfaction on those. **Still unfixed at the end of the data** |
| 20 Oct 2025 | Mobile app v4.0 release | App crash and PDF tickets spike for 3 weeks |
| 22 Dec 2025 to 2 Jan 2026 | Holidays | Volume down about 35% |
| 9 Feb 2026 | Payment processor migration | "Client's card declined" tickets about 2.5x for 4 weeks |
| 15 Jun 2026 | Price-increase email sent | Billing, refund and cancellation tickets up about 120% through July and August |
| **1 Jul 2026** | **Starter and Pro prices go up** | Downgrades and cancellations peak. **Still elevated at the end of the data** |
| Ongoing | **Documentation gaps** | Repeat how-to tickets on: setting up recurring invoices, connecting QuickBooks/Xero, adding VAT, setting late fees. These are the "top fixable gaps" |

Acute problems (QuickBooks bug, app crash, processor migration) are fixed within 3 to 4 weeks. Chronic problems (documentation gaps, the bot failing on payments) and the recent price increase are still live when the data ends: those are what the review recommends acting on now.

**Everyday rhythms:**
- Mondays about 25% busier than average; weekends about 60% quieter
- Month-end invoicing peak: last 3 and first 2 days of each month about 30% busier
- Customer base grows about 2.5% a month, so ticket volume grows too
- Business customers get faster replies than Free (they have priority)

## 8. The data

**Size:** 1 Apr 2025 to 30 Sep 2026 (18 months, six full quarters), about 10,000 customers, about 50,000 tickets.

**Files** (generated by `src/generate_data.py`, saved in `data/raw/`):

| File | What it is |
|---|---|
| `customers.csv` | One row per business customer |
| `tickets.csv` | The helpdesk export: one row per ticket |
| `answer_key.csv` | True category per ticket. Kept separate, used only to score the AI classification |

**customers.csv**

| Column | Example | Notes |
|---|---|---|
| customer_id | 10234 | Unique |
| business_name | Brightline Studio | Fake, from Faker |
| business_type | agency | freelancer, agency, trades, retail |
| plan | pro | free, starter, pro, business (current plan) |
| country | UK | US, UK, CA |
| signup_date | 2024-06-12 | |
| monthly_payment_volume | 8400.00 | Average card payments received per month, in local currency |

**tickets.csv**

| Column | Example | Notes |
|---|---|---|
| ticket_id | 500123 | Unique |
| customer_id | 10234 | Links to customers |
| created_at | 2025-08-11 09:42:00 | |
| first_response_at | 2025-08-11 09:43:10 | Empty if no reply yet |
| resolved_at | 2025-08-12 14:05:00 | Empty if still open |
| status | solved | open, pending, solved |
| channel | chat | email, chat, web_form |
| priority | normal | low, normal, high, urgent |
| subject | Client says card keeps failing | Customer's words |
| body | Hi, my client tried to pay invoice #1042 three times... | Customer's words; the AI classifies this |
| tags | payments, card | Agent tags: messy, sometimes empty |
| first_handler | ai_bot | ai_bot or human |
| escalated | 1 | 1 if the bot handed it to a human |
| final_tier | tier2 | bot, tier1, tier2, tier3 |
| reopened | 0 | 1 if the customer came back unresolved |
| reply_count | 4 | Back-and-forth messages |
| csat_rating | 2 | 1 to 5, empty if no survey answer (about 80% empty) |

## 9. Key metrics (definitions)

| Metric | Definition |
|---|---|
| Ticket volume | Tickets created per day/week/month |
| Contact rate | Tickets per 1,000 customers per month (fair comparison as customers grow) |
| First response time (FRT) | first_response_at minus created_at |
| Resolution time | resolved_at minus created_at |
| Reopen rate | Share of solved tickets that were reopened |
| Escalation rate | Share of bot-handled tickets passed to a human |
| Bot containment rate | Share of bot-handled tickets resolved without a human |
| CSAT | Average rating, and share of 4s and 5s, among tickets with a rating |
| SLA hit rate | Share of tickets answered within the plan's target |
| Cost per ticket | Assumed handling cost by final tier (below) |

**Cost assumptions** (invented, stated openly in the report):

| Final tier | Cost per ticket |
|---|---|
| Bot only | $0.80 |
| Tier 1 | $7 |
| Tier 2 | $15 |
| Tier 3 (engineering) | $45 |

## 10. Questions the project answers

1. **Headline:** What are the top three fixable product or documentation gaps causing the most avoidable tickets, and what does each cost per year?
2. Did Fern Assist reduce cost, and where does it fail customers? (Which categories does it escalate or get wrong?)
3. What did the price increase and the processor migration cost in extra tickets and churn risk?
4. Are we meeting SLAs by plan? Are paying customers getting the service they pay for?
5. Which customers are at risk (repeat contacts, reopens, low CSAT) and how much monthly revenue do they represent?
6. **How quickly would each issue have been detected with weekly monitoring?** For each event: when it started, when a simple weekly control chart would have flagged it, and how many tickets (and dollars) earlier detection would have saved.

## 11. Analysis framing and limitations

**Framing:** an 18-month support review covering 1 Apr 2025 to 30 Sep 2026, prepared in November 2026. Results are reported by month and by quarter. Where seasonality matters (tax season, holidays), a quarter is compared with the same quarter a year earlier rather than the quarter before.

**Limitations (stated in the report):**
- **Data cut-off:** the data ends on 30 Sep 2026, the last complete quarter when the export was taken. October 2026 is excluded because it was incomplete, so the effects of the July price increase are only partly visible.
- **Synthetic data:** all tickets and customers are generated. Patterns and events were designed to be realistic; findings demonstrate the method, not a real company's results.
- **Cost assumptions:** cost per ticket and revenue figures are assumptions, stated in section 9.
- **CSAT bias:** only about 20% of customers answer the survey, and unhappy customers answer more often, so CSAT is a signal, not a precise measure.
- **AI classification:** labels come from a random sample of 3,000 to 5,000 tickets, scored against an answer key; error rates are reported.

## 12. Glossary

| Term | Meaning |
|---|---|
| Invoice | A bill a business sends its client |
| Recurring invoice | An invoice sent automatically on a schedule |
| Payment processor | The company that actually moves card money behind the scenes |
| Card decline | The client's bank refuses the card payment |
| Deposit (payout) | Money moving from Fernledger to the customer's bank account |
| Dispute / chargeback | The client asks their bank to reverse a payment |
| Refund | Money returned, by the customer to their client or by Fernledger to the customer |
| ACH / BACS | Bank transfer systems in the US / UK |
| VAT / GST / sales tax | Taxes added to invoices in the UK / Canada / US |
| Bank feed | Automatic import of bank transactions into accounting software |
| MRR | Monthly recurring revenue: what customers pay per month in subscriptions |
| Churn | Customers cancelling |
| Downgrade | Moving to a cheaper plan |
| SLA | Service level agreement: the promised response time |
| Containment | The bot solved it without a human |
| Escalation | Passed from the bot (or Tier 1) to a higher tier |
| CSAT | Customer satisfaction score from a post-ticket survey |
