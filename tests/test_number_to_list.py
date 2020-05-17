import pytest
from pyproblems.number_to_list import number_to_list_digits

def test_number_to_list_valid():
    numbers = [123, 456, 123456, 9999, 9876, 123456789]
    return_values = [[1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], [9, 9, 9, 9],
                    [9, 8, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    for value, ret_val in zip(numbers, return_values):
        assert ret_val == number_to_list_digits(value)

def test_number_to_list_invalid():
    numbers = ["123", None, "abcd", [1, 2, 3], {1, 2, 3}, {123}]

    for value in numbers:
        with pytest.raises(ValueError):
            number_to_list_digits(value)