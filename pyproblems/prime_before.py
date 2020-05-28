'''Given a number, returns the prime number that comes first when we count backward'''
from pyproblems.prime import is_prime
from pyproblems.utility import is_int

def prime_before(number):
    '''The Function will return the prime number that comes first
    when we count from backwards of the given number
    Note: The number passed should be greater than 2'''
    if not is_int(number):
        raise TypeError("Unsupported format")
    if number <= 2:
        raise ValueError('Invalid input')
    for i in range(number-1, 1, -1):
        if is_prime(i):
            return i
    #This return will never be executed
    return None
