"""
Layer 2: DAILY TICKET VOLUME

GOAL
Decide how many support tickets arrive on each day from 1 Apr 2025
to 30 Sep 2026 (548 days). Later layers give each ticket its details
(category, channel, text...). This layer only decides HOW MANY per day.

WHY NOT JUST PICK A RANDOM NUMBER EACH DAY?
Support volume follows patterns:
  - More customers -> more tickets (the business is growing)
  - Mondays are busy, weekends are quiet
  - Month-end is busy (customers send invoices)
  - Holidays are quiet

THE FORMULA
  expected tickets on a day = active customers x contact rate x multipliers

  active customers : how many customers had signed up on or before that day
                     (we assume nobody cancels; noted as a limitation)
  contact rate     : average tickets per customer per day, CALCULATED in step C
                     from the target (50,000 in the brief minus about 1,000
                     event tickets = 49,000) -> comes out at about 0.012,
                     i.e. about 1 ticket per customer every 3 months
  multipliers      : boosts or cuts for rhythms
                     Monday x1.25 | Tue-Thu x1.05 | Fri x1.0 | Sat-Sun x0.4
                     month-end (last 3 + first 2 days of a month) x1.3
                     holidays (22 Dec to 2 Jan) x0.65

ADDING RANDOMNESS (POISSON)
Two Mondays with the same expected number (say 120) never get exactly
120 tickets each: one might get 112, another 131. A Poisson
distribution models this. It's the standard model for counting
independent arrivals in a fixed period: calls per hour, customers
per day, tickets per day. Its spread grows with the expected value.

STEPS IN THIS FILE
  A. Active customers on each day   (count signups, fill gaps, running total)
  B. Multipliers for each day       (weekday, month-end, holidays)
  C. Expected tickets, then actual tickets with Poisson randomness
  D. Checks: total, weekday pattern, monthly growth
"""

# STEP A: ACTIVE CUSTOMERS ON EACH DAY
# A customer can only raise a ticket after they sign up.
# So for every day we need: how many customers existed by then?
# Plan: (1) count signups per day, 
#       (2) fill in days with no signups,
#       (3) running total -> customers so far.

import pandas as pd
import numpy as np
rng = np.random.default_rng(42)


customers = pd.read_csv("data/raw/customers.csv") #Load customers
signup = pd.to_datetime(customers["signup_date"]) #convert date to correct format

#count customers signup each day and sort by date
signup_per_day = signup.value_counts().sort_index()
#view signups
#print(signup_per_day.head())

# Step A2: fill in the missing days, with reindex
# Make a full calendar: every single day from first signup (2019-06-01)
# to the end of the data 2026-09-30)
all_days = pd.date_range("2019-06-01", "2026-09-30")

# Step A2: add the signups onto full calendar
# Days with no signups get 0 instead of missing value
signup_full = signup_per_day.reindex(all_days, fill_value=0)

# Step A3: use cumsum() to calculate the running total
active_all = signup_full.cumsum()
#print(active_all)

# Step A4: Keep the analysis window
#Customers who signup before April 2025 are still counted
days = pd.date_range("2025-04-01", "2026-09-30")

#slice from April 1st 2025 to last date
active = active_all.loc["2025-04-01":]

# Check for 548 days, 6,370 customers on day 1, and around 10,000 on last day
print(len(active), "days")
print(active.iloc[0], "active customers on 1 April 2025")
print(active.iloc[-1], "Active customer on 30 Sep 2026")

# STEP B: MULTIPLIERS FOR EACH DAY
# Each day gets a multiplier that scales its expected tickets up or down.
#   1.0 = a normal day | 1.25 = 25% busier | 0.4 = 60% quieter
# Three separate rhythms, multiplied together:
#   weekday   : Mon x1.25, Tue-Thu x1.05, Fri x1.0, Sat-Sun x0.4
#   month-end : last 3 days + first 2 days of a month x1.3
#               (customers send and chase invoices then)
#   holidays  : 22 Dec to 2 Jan x0.65
# Example: a Monday that is also month-end -> 1.25 x 1.3 = 1.625
#          (about 60% busier than a normal day)

# B1. Weekday multiplier: a dictionary from day number (Mon=0 ... Sun=6)
weekday_multiplier = {0:1.25, 1:1.05, 2:1.05, 3:1.05, 4:1.00, 5:0.40, 6:0.40}
# lookup each day's value with .map
weekday_mult = pd.Series(days.day_of_week).map(weekday_multiplier).to_numpy()

#B2: Month-end multiplier: last 3 days + first 2 days of a month x1.3
#first 2 days: days.day <=2
# last 3 days: days.days_in_month - days.day < 3
month_end_mult = np.where((days.day <=2) | (days.days_in_month - days.day < 3), 1.3, 1.0)

#B3 Holiday multiplier: 22 Dec to 2 Jan x0.65
# 22- 31 Dec: days.month==12 & days.day >= 22
# 1-2 Jan: days.month ==1 & days.day <=2

holiday_mult = np.where (((days.month==12) & (days.day >= 22)) | 
                         ((days.month ==1) & (days.day <=2)), 0.65, 1.0)

multiplier = weekday_mult * month_end_mult * holiday_mult

#verify the dates
check = pd.DataFrame({
    "date": days,
    "weekday": days.day_name(),
    "weekday_mult": weekday_mult,
    "month_end_mult": month_end_mult,
    "holiday_mult": holiday_mult,
    "multiplier": multiplier
})

print(check[(check["date"]>= "2025-12-22") & (check["date"] <= "2026-01-04")])

# STEP C: EXPECTED AND ACTUAL TICKETS PER DAY
# C1. Expected tickets = active customers x contact rate x multiplier
#     It's smooth and has decimals, so it isn't realistic yet.
# C2. Actual tickets = a random whole number drawn around the expected value,
#     using a Poisson distribution (the standard model for counting arrivals).
#     Expected 96.4 might become 91 one day and 103 the next.
#     Poisson's spread grows with the expected value:
#     standard deviation = square root of the expected value
#     (expected 100 -> most days between about 80 and 120).

# Contact rate = each customer's chance of raising a ticket on a given day.
target_total_tickets = 50_000 #from brief
event_tickets_estimate = 1_000 #my estimate of extra tickets for events such as updates/bugs
target_everyday_tickets = target_total_tickets - event_tickets_estimate

#each day contributes to the total tickets: active customers x Multipliers
weighted_customer_days = (active.to_numpy() * multiplier).sum()

# total tickets = contact rate x weighted_customer_days
contact_rate = target_everyday_tickets /weighted_customer_days

print(round(weighted_customer_days), "weighted_customer_days")
print(round(contact_rate, 4), "contact rate")
print(round(1/contact_rate), "average days between tickets per customer")

# C1: expected tickets per day
# active customer x contact rate x multiplier
expected = active.to_numpy()*contact_rate*multiplier

# C2: Actual tickets per day using poisson to draw around each expected value
tickets = rng.poisson(expected)

# C3: combine to one daily table to confirm
daily = pd.DataFrame({
    "date": days,
    "active_customers": active.to_numpy(),
    "multiplier": multiplier,
    "expected": expected,
    "tickets": tickets
})

#confirm
print(daily.head(10))
print(daily["tickets"].sum(), "tickets in total")

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
average_tickets_weekday = daily.groupby(daily["date"].dt.day_name())["tickets"].mean().reindex(day_order)
print("Average ticket distribution per week \n ", average_tickets_weekday)

# Total tickets distribution per month per year
tickets_per_month = daily.groupby(daily["date"].dt.to_period("M"))["tickets"].sum()
print(" \n Total tickets distribution per month per year \n ", tickets_per_month)
# CALENDAR EFFECT: November 2025 (2,380) is LOWER than both October (2,656)
# and December (2,558), even though December has the holiday dip.
# Why: months have different numbers of weekend days and busy days.
#   - November 2025 has 10 weekend days, and its first 2 days
#     (busy month-start days) fall on a weekend, so the boost is wasted.
#   - December 2025 has only 8 weekend days and starts on a Monday,
#     so it gets more busy days, which outweighs the holiday dip.

# Busiest and quietest days
print("\n busiest days \n ", daily.nlargest(5, "tickets"))

print("\n Quietest days \n", daily.nsmallest(5, "tickets"))

# Quietest: all weekends in 2025 (20 to 24 tickets, expected about 31).
#   the holiday weekends (27-28 Dec, expected about 25) are NOT
#   in the bottom five, even though their expected value is the lowest.
#   Why: random variation. A few normal weekends drew unusually low numbers.

"""
Layer 3:  TICKET DETAILS AND EVENTS
Create one row per ticket (about 50,000 rows) and give each ticket its details
"""

# PART A: ONE ROW PER TICKET
# A1: Expand the daily counts: A day with 95 tickets becoems 95 rows
# A2: Assign each ticket a time of day(Assuming 13:00-17:00 UTC is the busiest; 
#     both UK and US customers are working)
# Give each ticket a customer who had alreadt signed up by that day

#  A1. Repeat each day's date and active-customer count by its number of tickets
ticket_date = np.repeat(daily["date"], daily["tickets"]).to_numpy()
active_for_ticket = np.repeat(daily["active_customers"], daily["tickets"]).to_numpy()
# number of tickets
n_tickets = len(ticket_date)
#ticket id starting from 500001
ticket_id = np.arange(500_001,500_001 + n_tickets)

#check
print(n_tickets)
print(len(ticket_date), len(active_for_ticket))
print(ticket_date[:5])
print(active_for_ticket[:5])

# A2. TIME OF DAY FOR EACH TICKET
# Tickets don't arrive evenly over 24 hours: customers contact support
# while they are working. All times are stored in UTC (world standard time).
#
# Who is awake and working at each UTC hour (approximate, ignoring
# daylight saving; winter offsets: UK = UTC, US Eastern = UTC-5,
# US Pacific = UTC-8):
#
# | UTC hours | UK local    | US Eastern  | US Pacific  | Who is working              | Level | Weight |
# |-----------|-------------|-------------|-------------|-----------------------------|-------|--------|
# | 00 - 06   | 00:00-06:00 | 19:00-01:00 | 16:00-22:00 | Almost nobody (US West ends)| low   |   1   |
# | 07 - 12   | 07:00-12:00 | 02:00-07:00 | 23:00-04:00 | UK only                     | mid   |   5   |
# | 13 - 17   | 13:00-17:00 | 08:00-12:00 | 05:00-09:00 | UK + US East                | high  |   10    |
# | 18 - 21   | 18:00-21:00 | 13:00-16:00 | 10:00-13:00 | US East + US West           | high  |   10    |
# | 22 - 23   | 22:00-23:00 | 17:00-18:00 | 14:00-15:00 | US West (+ US East ending)  | low   |   1   |
#
# Assumptions:
#   - Customer split from the brief: US 60%, UK 25%, Canada 15%.
#     Canada shares US time zones, so 75% of customers are North American.
#     That's why 18:00-21:00 UTC (US afternoon) stays HIGH even though
#     the UK has finished work: the biggest group is still working.
#   - Night hours are LOW, not zero: some freelancers work late or
#     send invoices in the evening.
#   - Daylight saving shifts real times by 1 hour for part of the year;
#     ignored here for simplicity (noted as a limitation).
#   - The weight numbers only matter relative to each other:
#     a weight of 10 means 10x as many tickets as a weight of 1.

hour_weights = np.array(
    [1]* 7 +  # 00-06: low (7 hours)
    [5] * 6 + # 07-12: mid (6 hours)
    [10] * 5 + # 13-17: high (5 hours)
    [10] * 4 + # 18-21: high (4 hours)
    [1] * 2 # 22-23: low (2 hours)
    )

#weights  as a probability
p_hour = hour_weights/hour_weights.sum()

#one hour per ticket, picked with the probability above
hours = rng.choice(24, size = n_tickets, p=p_hour)

#a random minute and second for each ticket
minutes = rng.integers(0,60, size = n_tickets)
seconds = rng.integers(0,60, size = n_tickets)

#check
print(len(hour_weights), p_hour.sum())
print(np.bincount(hours)) #check the shape of the ticket

#combine date +hour + minute + seconds into one full timestamp per ticket 
# using pd.to_timedelta(array, unit)
# where unit can be "h", "m" or "s"
created_at = (pd.to_datetime(ticket_date) #convert ticket_date to datetime
+ pd.to_timedelta(hours, unit='h') #add hours
+ pd.to_timedelta(minutes, unit='m') #add minutes
+ pd.to_timedelta(seconds, unit='s')).sort_values()#add seconds
# Sorted so tickets are in time order (ticket ids then increase over time, like a real helpdesk).
print(created_at[:5])