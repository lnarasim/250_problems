import pytest
from pyproblems.abundant_number import is_abundant

def test_true():
    assert is_abundant(12)==True
    assert is_abundant(18)==True
    assert is_abundant(20)==True
    assert is_abundant(30)==True
    assert is_abundant(945)==True
    assert is_abundant(1158)==True

def test_false():
    assert is_abundant(13)==False
    assert is_abundant(45)==False
    assert is_abundant(28)==False#this is perfect number
    assert is_abundant(941)==False

def test_unsupported():
    with pytest.raises(TypeError) as err:
        is_abundant([12])#True value but in a list
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant((12,20,30))#true values in a tuple
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant('Jothi')#String
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant({'first':2,'second':12})#Random valuse inside a dict
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant([12,30,945])#True values inside a list
        assert err.value.args[0] == "unsupported format, Enter an Integer"