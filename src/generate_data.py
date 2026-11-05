"""
Generate about 10,000 customers matching the brief:
    plans: 45% Free, 30% Starter, 18% Pro, 7% Business
    countries: 60% US, 25% UK, 15% CA
    business types: 45% freelancer, 25% agency, 18% trades, 12% retail
    signup dates growing about 2.5% a month
    payment volumes inline with each plan

"""
import pandas as pd
import numpy as np

rgn = np.random.default_rng(42) #using seed to ensure same random numbers are generated
n_customers = 10000 #number of rows

#generate randomised data for each column

customer_id = np.arange(10000, 10000+ n_customers)
business_type =rgn.choice(['freelancer', 'agency', 'trades', 'retail'], size=n_customers, p=[0.45,0.25,0.18,0.12])
plan = rgn.choice(['free', 'starter', 'pro', 'business'], size=n_customers, p=[0.45,0.30,0.18,0.07])
print(pd.Series(plan).value_counts(normalize=True))
country =rgn.choice(['US', 'UK', 'CA'], size=n_customers, p=[0.60,0.25,0.15])

#------------Signup dates
#The brief says the CUSTOMER BASE grows about 2.5% a month:
#about 6,500 customers in Apr 2025 -> about 10,000 by Sep 2026.

#But this code controls something different: how many NEW SIGNUPS happen each month. 
#The customer base is all signups added up since 2019, so the two growth rates are not the same number.

#To find the right signup growth rate, I tested several values and counted how many customers existed by Apr 2025:
#    1.5% a month -> about 6,800 customers
#    2.0% a month -> about 6,400 customers  (closest to the brief)
#    2.5% a month -> about 5,950 customers  (too few)

#With 2% signup growth, the base goes from about 6,400 (Apr 2025) 
#to 10,000 (Sep 2026), which is about 2.5% a month. 
#(10,000 / 6,400) ** (1/18) - 1 ~ 0.025

#Simplification: no customer ever cancels (no churn), so every signup stays in the base. Noted as a limitation.
monthly_signup_growth = 1.02
#'MS' -month start
months = pd.date_range(start='2019-06-01', end='2026-09-01', freq='MS')

# Growing weights: Month 0 gets weight 1, month 1 gets 1.02, month 2 gets 1.02 × 1.02, and so on
weights = monthly_signup_growth ** np.arange(len(months))
#turn weights into probability
prob = weights / weights.sum()
#months per customer
signup_month = rgn.choice(months,size=n_customers, p=prob)
#generate random days
days = rgn.integers(0,28, size=n_customers)
#combine months and days
signup_date = signup_month + pd.to_timedelta(days, unit='D')
#format signup_date
signup_date = signup_date.strftime('%Y-%m-%d') 
#check the output
signups = pd.Series(pd.to_datetime(signup_date))
print((signups < '2025-04-01').sum(), 'Customers before April 2025')
print((signups >= '2025-04-01').sum(), 'Customers after April 2025')
print(signups.dt.year.value_counts().sort_index())

 
#------------Monthly payment volume 

# monthly_payment_volume = money the customer's OWN clients pay them through
# Fernledger invoices each month (not what the customer pays Fernledger).
# Free-plan customers still get paid by their clients, and Fernledger earns a card fee on it, so they have payment volume too.

# Money is skewed ie most small businesses collect modest amounts and a few
# collect a lot (a long tail to the right). A lognormal distribution models
# this: no negative values, and a realistic number of big earners.

# Typical (median) monthly payment volume for each plan.
# Bigger businesses choose bigger plans, so they collect more.

median_volume_by_plan = {
    "free": 600,
    "starter": 2500,
    "pro": 8000,
    "business": 25000
}
# Look up each customer's median using their plan
# (e.g. a 'pro' customer gets 8000). Result: one number per customer.
median_volume = pd.Series(plan).map(median_volume_by_plan).to_numpy()

#Draw each customer's volume from a lognormal distribution centred on their plan's median.
#   mean  = log of the median
#   sigma = 0.8 -> how spread out values are (most within about 1/3x to 3x the median)
# Round to 2 decimals because it's currency.
monthly_payment_volume = np.round(rgn.lognormal(mean=np.log(median_volume), sigma=0.8),2)

# Check: the median volume per plan should be close to the targets above
check = pd.DataFrame({"plan": plan, "volume":monthly_payment_volume})
print(check.groupby("plan")["volume"].median().round(0))


#----------business_name
# Use Faker to generate fake business names

from faker import Faker
Faker.seed(42) #same name evry run
fake = Faker()
#generate the names
business_name = [fake.company() for _ in range(n_customers)]

#compile the array to dataframe
customers = pd.DataFrame({
    "customer_id": customer_id,
    "business_name": business_name,
    "business_type": business_type,
    "plan": plan,
    "country": country,
    "signup_date": signup_date,
    "monthly_payment_volume": monthly_payment_volume}
)

#save to csv
customers.to_csv("data/raw/customers.csv", index=False) # index=False stops pandas adding an extra column of row numbers

#inspect dataframe
print(customers.shape)
print(customers.head(2))
print(customers.isna().sum())