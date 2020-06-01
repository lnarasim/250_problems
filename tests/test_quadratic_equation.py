import pytest
from pyproblems.quadratic_equation import quadratic_equation

def test_quadratic_equation_real_and_distinct():
    assert quadratic_equation(1,-3,-10) == (5,-2)
    assert quadratic_equation(3,2,-1) == ((1/3),-1)
    assert quadratic_equation(1,-18,45) == (15,3)
 
def test_quadratic_equation_real_and_equal():
    assert quadratic_equation(6,-12,6) == (1,1)
    assert quadratic_equation(4,-4,1) == (0.5,0.5)
    assert quadratic_equation(1,-12,36) == (6,6)

def test_quadratic_equation_complex():
    assert quadratic_equation(1,4,5) == ((-2.0+1.0j),(-2.0-1.0j))
    assert quadratic_equation(1,-6,13) == ((3.0+2.0j),(3.0-2.0j))
    
