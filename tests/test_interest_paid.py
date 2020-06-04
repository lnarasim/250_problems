from pyproblems.interest_paid import calc_int_paid
import pytest

def test_interest_paid():
    assert calc_int_paid(2000000,10.2,10) == 1198258
    assert calc_int_paid(500000,13.99,5) == 197892
    assert calc_int_paid(4500000,7.99,18) == 3998758
    assert calc_int_paid(700000,10,8) == 319704
    assert calc_int_paid(10000,12.05,1) == 665
    assert calc_int_paid(350000,13.99,3) == 80577
    assert calc_int_paid() == 16162
    assert calc_int_paid(1000000,10,12) == 720913

def test_calc_int_paid_invalid_1():
    with pytest.raises(ValueError):
        calc_int_paid(20000,-5,10) #negative interest rate
def test_calc_int_paid_invalid_2():
    with pytest.raises(TypeError):
        calc_int_paid(20000,-5,10.5) #To check if the types are getting checked first
def test_calc_int_paid_invalid_3():
    with pytest.raises(TypeError):
        calc_int_paid((1000,10,1)) #There is a tuple in the place of principle
def test_calc_int_paid_invalid_4():    
    with pytest.raises(TypeError):
        calc_int_paid(30000,13.5,2.8) #Year as float
def test_calc_int_paid_invalid_5():    
    with pytest.raises(ValueError):
        calc_int_paid(500000,14.99,-5) #Year as a negative value
def test_calc_int_paid_invalid_6():    
    with pytest.raises(TypeError):
        calc_int_paid('4000000','12','5') #string arguments