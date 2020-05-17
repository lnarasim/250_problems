"""This module contains functions that works on palindrom"""
from pyproblems.utility import is_str

def is_palindrome(s_param):
    '''Returns True if passed string is palindrome, False if
    the string is not a palindrome'''

    if not is_str(s_param):
        raise TypeError(f"Unsupported Type f{type(s_param)}")

    return s_param == s_param[::-1]
    