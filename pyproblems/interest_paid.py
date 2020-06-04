'''This program is to find out the interest paid over the term of the loan'''
from pyproblems.utility import is_float
from pyproblems.utility import is_int

def calc_int_paid(amt_borrowed: "Money borrowed" = 100000, int_rate: "interest rate per year" = 10,
                  term: "Term of the loan" = 3):
    '''The function will calculate the emi for the loan and then returns the interest amount
    paid during the term of the loan'''
    for i in (amt_borrowed, term):
        if not is_int(i):
            raise TypeError(f'Unsupported format,{type(i)} in the place of "int"')
    if not is_float(int_rate) and not is_int(int_rate):
        raise TypeError(f'Unsupported format,{type(int_rate)} in the place of "int" or "float"')
    for i in (amt_borrowed, int_rate, term):
        if i < 1:
            raise ValueError("Invalid Entry")

    #Encapsulating of the function to calculate emi
    def calc_emi(amt_borrowed, int_rate, term):
        monthly_int = int_rate/(12 * 100) #converting the yearly interest to monthly
        months = term*12
        present_value = 1/(1+monthly_int) #Finding out present value for Re.1
        v_n = present_value**months
        annuity = (1-v_n)/monthly_int #annuity for the term
        return amt_borrowed / annuity

    #The below method is to calculate the total interest from the loan schedule

    emi = calc_emi(amt_borrowed, int_rate, term)
    interest_amt = amt_borrowed*(int_rate/(12 * 100))
    total_interest = interest_amt
    principle_amt = emi - interest_amt
    loan_outstanding = amt_borrowed-principle_amt

    while loan_outstanding > 0:
        interest_amt = loan_outstanding*(int_rate/(12 * 100))
        total_interest += interest_amt
        principle_amt = emi - interest_amt
        loan_outstanding = loan_outstanding - principle_amt

    return round(total_interest)
