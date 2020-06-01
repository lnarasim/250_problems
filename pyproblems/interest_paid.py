'''This program is to find out the interest paid over the term of the loan'''
from pyproblems.utility import is_float
from pyproblems.utility import is_int

def calc_int_paid(principle: "Money borrowed" = 100000, interest: "interest rate per year" = 10,
                  years: "Term of the loan" = 3):
    '''The function will calculate the emi for the loan and then returns the interest amount
    paid during the term of the loan'''
    for i in (principle, years):
        if not is_int(i):
            raise TypeError(f'Unsupported format,{type(i)} in the place of "int"')
    if not is_float(interest) and not is_int(interest):
        raise TypeError(f'Unsupported format,{type(interest)} in the place of "int" or "float"')
    for i in (principle, interest, years):
        if i < 1:
            raise ValueError("Invalid Entry")

    monthly_int = interest / (12*100) #converting the yearly interest to monthly
    months = years * 12
    present_value = 1/(1 + monthly_int) #Finding out present value for Re.1
    v_n = present_value ** months
    annuity = (1 - v_n) / monthly_int #annuity for the term
    emi = principle/annuity

    #The below method is to calculate the total interest from the loan schedule
    interest_amt = principle*(interest/(12*100))
    total_interest = interest_amt
    principle_amt = emi - interest_amt
    loan_outstanding = principle-principle_amt

    while loan_outstanding > 0:
        interest_amt = loan_outstanding*(interest/(12*100))
        total_interest += interest_amt
        principle_amt = emi - interest_amt
        loan_outstanding = loan_outstanding - principle_amt

    return round(total_interest)
