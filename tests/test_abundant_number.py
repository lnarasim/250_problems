import pytest
from pyproblems.abundant_number import is_abundant_number

def test_abundant_number_true():
    assert is_abundant_number(12)
    assert is_abundant_number(18)
    assert is_abundant_number(20)
    assert is_abundant_number(30)
    assert is_abundant_number(945)
    assert is_abundant_number(1158)

def test_abundant_number_false():
    assert not is_abundant_number(13)
    assert not is_abundant_number(45)
    assert not is_abundant_number(28)#this is perfect number
    assert not is_abundant_number(941)

def test_abundant_number_unsupported():
    with pytest.raises(TypeError) as err:
        is_abundant_number([12])#True value but in a list
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant_number((12,20,30))#true values in a tuple
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant_number('Jothi')#String
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant_number({'first':2,'second':12})#Random valuse inside a dict
        assert err.value.args[0] == "unsupported format, Enter an Integer"
    with pytest.raises(TypeError) as err:
        is_abundant_number([12,30,945])#True values inside a list
        assert err.value.args[0] == "unsupported format, Enter an Integer"