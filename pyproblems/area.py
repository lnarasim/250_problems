'''This program will return area of square or rectangle
based on the passed arguments'''
from pyproblems.utility import is_int
from pyproblems.utility import is_float

def area(length, *b):
    '''This function will take passed arguments and return
    area of square if b is not given, else it will
    return the area of rectangle'''
    if not (is_int(length) or is_float(length)):
        raise TypeError(f"Unsupported type,'{type(length)}' in the place of 'int' or 'float'")
    if length <= 0:
        raise ValueError("Invalid entry")
    if b:
        if len(b) > 1:
            raise ValueError("unpacking cannot be done")
        if not (is_int(b[0]) or is_float(b[0])):
            raise TypeError(f"Unsupported type,'{type(b[0])}' in the place of 'int' or 'float'")
        if b[0] <= 0:
            raise ValueError("Invalid entry")
        breadth, = b
        if length != breadth:
            return length*breadth
    return length*length
