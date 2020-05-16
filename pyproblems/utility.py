'''This module contains all utility functions'''
def is_int(number):
    '''This function returns True is the number is an integer,
    otherwise false'''
    if isinstance(number, int) and (not isinstance(number, bool)):
        return True
    return False
