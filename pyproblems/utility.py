def is_int(number):
    if isinstance(number, int) and (not isinstance(number, bool)):
        return True
    return False