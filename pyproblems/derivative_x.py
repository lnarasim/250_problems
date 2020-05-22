'''This program returns the derivative of "x" raised to the nth power,
where n ranges from "-infinity to +infinity"'''
from pyproblems.utility import is_int
def derivative_x_pow(dif, num):
    '''The function will return the nth derivative of "x" raised to the power of the given number'''
    for i in (dif, num):
        if not is_int(i):
            raise TypeError("unsupported format")
    if dif <= 0:
        raise ValueError("invalid entry, enter a valid number to differentiate")
    if (dif > num) and num in (0, 1):
        return 0
    if dif >= num > 0:
        return 1
    fore = 1
    index = num
    for _ in range(1, dif+1):
        fore = fore * index
        index = index-1
    return f'{fore}(x^{index})'
