'''This program is to find out the product of the prime factors of a given number'''
from pyproblems.utility import is_int
from pyproblems.prime import is_prime

def product_prime(number):
    '''This function returns the product of the numbers which are prime factors
    of a given number'''
    if not is_int(number):
        raise TypeError(f'unsupported format, {type(number)} is in the place of"integer"')
    if number <= 0:
        raise ValueError("pass an integer greater than 0")
    product = 1
    for i in range(2, number+1):
        if number % i == 0 and is_prime(i):
            product = product * i
    return product
    