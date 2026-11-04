--Fernledger support database
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS customers;

--creating customers table
CREATE TABLE customers (
customer_id INTEGER PRIMARY KEY,
business_name TEXT NOT NULL,
business_type TEXT NOT NULL CHECK(business_type IN ('freelancer', 'agency', 'trades', 'retail')), --checks for specific type
plan TEXT NOT NULL CHECK(plan IN ('free', 'starter', 'pro', 'business')),
country TEXT NOT NULL CHECK(country IN ('US', 'UK', 'CA')),
signup_date TEXT NOT NULL CHECK(signup_date IS date(signup_date)), --only accepts text that’s already a valid YYYY-MM-DD date
monthly_payment_volume REAL NOT NULL CHECK(monthly_payment_volume >= 0)
);

--create tickets table
CREATE TABLE tickets(
ticket_id INTEGER NOT NULL PRIMARY KEY,
customer_id INTEGER NOT NULL,
created_at TEXT NOT NULL CHECK(created_at IS datetime(created_at)),
first_response_at TEXT CHECK(first_response_at IS datetime(first_response_at)),
resolved_at TEXT CHECK(resolved_at IS datetime(resolved_at)),
status TEXT NOT NULL CHECK(status IN ('open', 'pending', 'solved')),
channel TEXT NOT NULL CHECK(channel IN ('email', 'chat', 'web_form')),
priority TEXT NOT NULL CHECK (priority in ('low', 'normal', 'high', 'urgent')),
subject TEXT NOT NULL, 
body TEXT NOT NULL,
tags TEXT,
first_handler TEXT NOT NULL CHECK(first_handler IN ('ai_bot', 'human')),
escalated INTEGER NOT NULL CHECK(escalated IN (0, 1)),
final_tier TEXT NOT NULL CHECK(final_tier IN ('bot', 'tier1', 'tier2', 'tier3')),
reopened INTEGER NOT NULL CHECK(reopened IN (0,1)), 
reply_count INTEGER NOT NULL CHECK (reply_count >=0),
csat_rating INTEGER CHECK(csat_rating BETWEEN 1 AND 5),
CHECK(first_response_at >= created_at),
CHECK(resolved_at >= created_at),
FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

