import pytest
from pyproblems.factorial_number import factorial_num

def test_factorial_num():
    assert factorial_num(0) == 1
    assert factorial_num(1) == 1
    assert factorial_num(5) == 120
    assert factorial_num(50) == 30414093201713378043612608166064768844377641568960512000000000000

def test_invalid_factorial_1():
    with pytest.raises(TypeError):
        factorial_num('k')
def test_invalid_factorial_2():
    with pytest.raises(TypeError):
        factorial_num(5.0)
def test_invalid_factorial_3():
    with pytest.raises(ValueError):
        factorial_num(-1)
def test_invalid_factorial_4():
    with pytest.raises(TypeError):
        factorial_num(-5.0)
