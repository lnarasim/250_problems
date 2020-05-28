from pyproblems.compound_int import compound_interest
import pytest

def test_comp_int():
    assert compound_interest() == 144.90
    assert compound_interest(10000,4,10) == 4641.0
    assert compound_interest(400000,5,13.99) == 369828.1
    assert compound_interest(700000,10,8) == 811247.5
    assert compound_interest(10000,3,12.05) == 4068.1

def test_invalid_in_comp_int():
    with pytest.raises(TypeError):
        compound_interest(10000,2.5,7)#year as float

    with pytest.raises(TypeError):
        compound_interest((1000,5,10))#arguments inside a tuple

    with pytest.raises(TypeError):
        compound_interest([400000,5,14.99])#arguments inside a list

    with pytest.raises(ValueError):
        compound_interest(1000,-2,10)#year as negative value

    with pytest.raises(ValueError):
        compound_interest(100000,8,-14.99)#rate as negative value

    with pytest.raises(ValueError):
        compound_interest(-14000,8,7)#principle as negative value

    with pytest.raises(TypeError):
        compound_interest('10000')#principle as string