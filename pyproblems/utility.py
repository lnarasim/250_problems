'''This module contains all utility functions'''
def is_int(number):
    '''This function returns True is the number is an integer,
    otherwise false'''
    if isinstance(number, int) and (not isinstance(number, bool)):
        return True
    return False

def is_str(s_param):
    '''This function checks whether the passed parameter is a string'''
    return isinstance(s_param, str) and type(s_param) == str
