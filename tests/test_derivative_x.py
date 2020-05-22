import pytest
from pyproblems.derivative_x import derivative_x_pow

def test_dif_x():
    assert derivative_x_pow(2,3) == f'{6}(x^{1})'
    assert derivative_x_pow(2,-4) == f'{20}(x^{-6})'
    assert derivative_x_pow(3,3) == 1
    assert derivative_x_pow(1,3) == f'{3}(x^{2})'
    assert derivative_x_pow(2,1) == 0
    assert derivative_x_pow(2,0) == 0

def test_unsupported_diff_1():
    with pytest.raises(ValueError) as err:
        derivative_x_pow(0,1)
        assert err.value.args[0] =="invalid entry, enter a valid number to differentiate"
def test_unsupported_diff_2():
    with pytest.raises(ValueError) as err:
        derivative_x_pow(-1,2) 
        assert err.value.args[0] =="invalid entry, enter a valid number to differentiate"
def test_unsupported_diff_3():
    with pytest.raises(ValueError) as err:
        derivative_x_pow((0),(1)) 
        assert err.value.args[0] =="invalid entry, enter a valid number to differentiate"
def test_unsupported_diff_4():
    with pytest.raises(TypeError) as err:
        derivative_x_pow(False,True)
        assert err.value.args[0] =="unsupported format"
def test_unsupported_diff_5():
    with pytest.raises(TypeError) as err:
        derivative_x_pow(True,1) 
        assert err.value.args[0] =="unsupported format"
def test_unsupported_diff_6():
    with pytest.raises(TypeError) as err:
        derivative_x_pow([0,2,3],1) 
        assert err.value.args[0] =="unsupported format"