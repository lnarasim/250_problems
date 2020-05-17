from pyproblems.amstrong_number import is_amstrong_number
import pytest

def test_amstrong_number_valid():
    numbers = [2, 153, 1, 370, 371, 407, 1634, 8208, 9474, 3, 4, 5, 6, 7, 8, 0, 9]

    for number in numbers:
        assert is_amstrong_number(number) == True

def test_amstrong_number_invalid():
    numbers = [100, 200, 300, 10000]
    for number in numbers:
        assert is_amstrong_number(number) == False

def test_amstrong_number_different_types():
    inputs = {
        'list': [1, 2, 3, 4,],
        'dict': {1: 1, 2: 2},
        'bool': True,
        'set' : {1, 2, 3, 4},
        'None': None,
        'str': '123',
        'tuple': (1, 2, 3,4)
    }

    for _, value in inputs.items():
        with pytest.raises(TypeError):
            is_amstrong_number(value)

