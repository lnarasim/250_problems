from pyproblems.prime_factor_products import product_prime
import pytest
def test_product_prime_int():
 
    assert product_prime(144) == 6
    assert product_prime(146) == 146
  
def test_product_prime_float():
    with pytest.raises(TypeError):
        product_prime(250.5)

def test_product_prime_str():
    with pytest.raises(TypeError):
        product_prime('dummy')
                
def test_product_prime_bool_true():
    with pytest.raises(TypeError):
        product_prime(True)  

def test_product_prime_bool_false():
    with pytest.raises(TypeError):
        product_prime(False)  

def test_product_prime_zero():
    with pytest.raises(ValueError):
        product_prime(0)  

def test_product_prime_negative():
    with pytest.raises(ValueError):
        product_prime(-10)  

