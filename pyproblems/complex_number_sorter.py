'''This program will sort the passed sequence of complex number'''
from pyproblems.utility import is_int, is_float

def sort_complex_numbers(*complex_numbers):
    '''The function returns a sorted tuple of passed complex numbers
    based on the real part of those complex numbers'''
    for i in complex_numbers:
        if not is_int(i) and not is_float(i) and not isinstance(i, complex):
            raise TypeError("Unsupported format")
    list_complex = list(complex_numbers)
    list_complex.sort(key=lambda complex_num: complex_num.real)
    return tuple(list_complex)
