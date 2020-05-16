'''This module contains prime number related function'''
from pyproblems.utility import is_int

def is_prime(number):
    '''This fucntion returns True if the number is prime,
    False otherwise'''
    if not is_int(number):
        raise TypeError(f"Unsupported Type {type(number)}")

    for divisor in range(2, number):
        if number% divisor == 0:
            return False

    return True
