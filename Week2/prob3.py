# Write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. By a fixed monthly
# payment, we mean a single number which does not change each month, but 
# instead is a constant amount that will be paid each month.

MONTHS_IN_A_YEAR = 12

# Given by the problem
balance = 999999
annualInterestRate = 0.18

def get_monthly_interest_rate():
    return annualInterestRate/MONTHS_IN_A_YEAR

def monthly_mimimal_payment(balance, annual_interest_rate):
    monthly_interest_rate = 1 + get_monthly_interest_rate()
    coefficient = 0
    
    for _ in range(MONTHS_IN_A_YEAR):
        coefficient = (coefficient + 1) * monthly_interest_rate
        balance = balance * monthly_interest_rate
    
    return balance/coefficient

minimal_payment = monthly_mimimal_payment(balance, annualInterestRate)
print('Lowest Payment:', round(minimal_payment, 2))

assert minimal_payment == 90325.03

# Answer researched on 
# 'https://codereview.stackexchange.com/questions/142676/for-a-given-balance-and-an-annual-interest-rate-calculate-the-minimum-fixed-mon'