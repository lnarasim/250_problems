'''Finds out the number is a perfect number or not'''

def perfect_num(number):

    ''' The abouve function will return True if the number is Perfect number'''

    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("unsupported format")

    sum_divisors = 0

    for i in range(1, number):

        if number%i == 0:
            sum_divisors += i

    return bool((sum_divisors == number) and (sum_divisors != 1))
