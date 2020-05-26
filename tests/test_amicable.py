from pyproblems.amicable import amicable_numbers
import pytest
def test_amicable_number_true():
    assert amicable_numbers(220, 284)
    assert amicable_numbers(1184, 1210)
    assert amicable_numbers(2620, 2924)
    assert amicable_numbers(5020, 5564)
    assert amicable_numbers(6232, 6368)
    assert amicable_numbers(10744, 10856)
def test_amicable_number_not_true():
    assert not amicable_numbers(290,289)
def test_amicable_number_float():
    with pytest.raises(TypeError):
        amicable_numbers(250.5,450.5)  
def test_amicable_number_bool():
    with pytest.raises(TypeError):
        amicable_numbers(True,False)  
def test_amicable_number_zero():
    with pytest.raises(ValueError):
        amicable_numbers(0,0)  
def test_amicable_number_negative():
    with pytest.raises(ValueError):
        amicable_numbers(-10,-150)  