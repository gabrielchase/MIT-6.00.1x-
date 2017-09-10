# Write a program to calculate the credit card balance after one year if a 
# person only pays the minimum monthly payment required by the credit card company each month.

# Given by the problem
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def get_monthly_interest_rate():
    return annualInterestRate/12

def minimum_monthly_payment(prev_balance):
    return monthlyPaymentRate * prev_balance

def monthly_unpaid_balance(prev_balance):
    return prev_balance - minimum_monthly_payment(prev_balance)

def updated_balance_each_month(monthly_unpaid_balance):
    return monthly_unpaid_balance + (get_monthly_interest_rate() * monthly_unpaid_balance)

def get_remaining_balance(balance):
    minimum_payment = minimum_monthly_payment(balance)
    unpaid_balance = balance - minimum_payment
    return updated_balance_each_month(unpaid_balance)

def get_total_year_balance(balance, count):
    if count == 12:
        return balance
    else:
        new_balance = get_remaining_balance(balance)
        return get_total_year_balance(new_balance, count+1)


total_yearly_balance = round(get_total_year_balance(balance, 0), 2)

print('Remaining balance: {}'.format(total_yearly_balance))

assert total_yearly_balance == 361.61