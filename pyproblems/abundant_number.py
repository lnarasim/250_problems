'''This program is to find out the given number is an abundant number or not'''
from pyproblems.utility import is_int

def is_abundant_number(number):
    '''The above function will return True if the given number is an abundant number or not.
    Abundant Number: if the sum of the divisors(excluding the given number) of given number,
    exceeds the given number then it is said to be abundant
    Note: all prime numbers are not abundant.'''

    if not is_int(number):
        raise TypeError("unsupported format, Enter an Integer")

    sum_divisors = 1
    for i in range(2, number):
        if number%i == 0:
            sum_divisors += i

    return sum_divisors > number
