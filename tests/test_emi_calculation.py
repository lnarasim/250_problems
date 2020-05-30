from pyproblems.emi_calculation import emi_calc
import pytest

def test_emi_value():
    assert emi_calc(2000000,10.2,10) == 26652
    assert emi_calc(500000,13.99,5) == 11632
    assert emi_calc(4500000,7.99,18) == 39346
    assert emi_calc(700000,10,8) == 10622
    assert emi_calc(10000,12.05,1) == 889
    assert emi_calc(350000,13.99,3) == 11960
    assert emi_calc() == 3227
    assert emi_calc(1000000,10,12) == 11951

def test_emi_calc_invalid():
    with pytest.raises(ValueError):
        emi_calc(20000,-5,10) #negative interest rate

    with pytest.raises(TypeError):
        emi_calc(20000,-5,10.5) #To check if the types are getting checked first

    with pytest.raises(TypeError):
        emi_calc((1000,10,1)) #There is a tuple in the place of principle
    
    with pytest.raises(TypeError):
        emi_calc(30000,13.5,2.8) #Year as float
    
    with pytest.raises(ValueError):
        emi_calc(500000,14.99,-5) #Year as a negative value
    
    with pytest.raises(TypeError):
        emi_calc('4000000','12','5') #string arguments