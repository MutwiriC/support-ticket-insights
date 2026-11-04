--test1 good customer data
INSERT INTO customers(customer_id, business_name, business_type, plan, country, signup_date, monthly_payment_volume) VALUES (1, 'Brightline Studio', 'agency', 'pro', 'UK', '2024-06-12', 8400.00);
--test2 good ticket data for customer_id 1
INSERT INTO tickets (ticket_id, customer_id, created_at, first_response_at, resolved_at, status, channel, priority, subject, body, tags, first_handler, escalated, final_tier, reopened, reply_count, csat_rating) VALUES (1, 1, '2025-08-11 09:42:00', '2025-08-11 09:43:10', '2025-08-12 14:05:00', 'solved', 'chat', 'normal', 'Client card keeps failing', 'Hi, my client tried to pay invoice #1042 three times and the card keeps getting declined.', 'payments', 'ai_bot', 1, 'tier2', 0, 4, 2);

-- test3  Plan 'premium' does not exist: should be BLOCKED
INSERT INTO customers (customer_id, business_name, business_type, plan, country, signup_date, monthly_payment_volume) VALUES (2, 'Oak and Ivy', 'retail', 'premium', 'US', '2024-09-01', 1200.00);

-- test4 Signup date in the wrong format: should be BLOCKED
INSERT INTO customers (customer_id, business_name, business_type, plan, country, signup_date, monthly_payment_volume) VALUES (3, 'Kettle Plumbing', 'trades', 'starter', 'CA', '12/06/2024', 3100.00);

-- test5 Ticket for customer 999, who does not exist: should be BLOCKED
INSERT INTO tickets (ticket_id, customer_id, created_at, first_response_at, resolved_at, status, channel, priority, subject, body, tags, first_handler, escalated, final_tier, reopened, reply_count, csat_rating) 
VALUES (2, 999, '2025-08-11 09:42:00', '2025-08-11 09:43:10', '2025-08-12 14:05:00', 'solved', 'chat', 'normal', 'Client card keeps failing', 'Hi, my client tried to pay invoice #1042 three times and the card keeps getting declined.', 'payments', 'ai_bot', 1, 'tier2', 0, 4, 2);

-- test6 Resolved before it was created: should be BLOCKED
INSERT INTO tickets (ticket_id, customer_id, created_at, first_response_at, resolved_at, status, channel, priority, subject, body, tags, first_handler, escalated, final_tier, reopened, reply_count, csat_rating) VALUES (3, 1, '2025-08-11 09:42:00', '2025-08-11 09:43:10', '2025-08-10 14:05:00', 'solved', 'chat', 'normal', 'Client card keeps failing', 'Hi, my client tried to pay invoice #1042 three times and the card keeps getting declined.', 'payments', 'ai_bot', 1, 'tier2', 0, 4, 2);

-- test7 CSAT rating of 7 (allowed range is 1 to 5): should be BLOCKED
INSERT INTO tickets (ticket_id, customer_id, created_at, first_response_at, resolved_at, status, channel, priority, subject, body, tags, first_handler, escalated, final_tier, reopened, reply_count, csat_rating) VALUES (4, 1, '2025-08-11 09:42:00', '2025-08-11 09:43:10', '2025-08-12 14:05:00', 'solved', 'chat', 'normal', 'Client card keeps failing', 'Hi, my client tried to pay invoice #1042 three times and the card keeps getting declined.', 'payments', 'ai_bot', 1, 'tier2', 0, 4, 7);

-- 8. Escalated = 2 (only 0 or 1 allowed): should be BLOCKED
INSERT INTO tickets (ticket_id, customer_id, created_at, first_response_at, resolved_at, status, channel, priority, subject, body, tags, first_handler, escalated, final_tier, reopened, reply_count, csat_rating) VALUES (5, 1, '2025-08-11 09:42:00', '2025-08-11 09:43:10', '2025-08-12 14:05:00', 'solved', 'chat', 'normal', 'Client card keeps failing', 'Hi, my client tried to pay invoice #1042 three times and the card keeps getting declined.', 'payments', 'ai_bot', 2, 'tier2', 0, 4, 2);