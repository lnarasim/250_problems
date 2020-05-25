from pyproblems.sep_odd_eve import sep_odd_eve
import pytest

def test_sep_odd_eve():
    assert sep_odd_eve([0,1,2,3,4,5,6,7,8,9,10]) == [[1,3,5,7,9],[0,2,4,6,8,10]]
    assert sep_odd_eve([10,40,80,50,70,60]) == [[],[10,40,80,50,70,60]]
    assert sep_odd_eve([41,51,61,87,75,93]) == [[41,51,61,87,75,93],[]]

def test_unsup_format_1():
    with pytest.raises(TypeError) as err:
        sep_odd_eve((1,2,4,5,7,8))#tuple containing the integers
        assert err.value.args[0] == "unsupported format, pass a list"
def test_unsup_format_2():
    with pytest.raises(TypeError) as err:
        sep_odd_eve({1,2,4,5,7,8})#set containing the integers
        assert err.value.args[0] == "unsupported format, pass a list"
def test_unsup_format_3():
    with pytest.raises(TypeError) as err:
        sep_odd_eve([1,2,'j',5,7,8])#a string within the integers
        assert err.value.args[0] == "unsupported format, pass integers inside the list"
def test_unsup_format_4():
    with pytest.raises(TypeError) as err:
        sep_odd_eve([1,2,4,5,7.0,8])#a float within the integers
        assert err.value.args[0] == "unsupported format, pass integers inside the list"
def test_unsup_format_5():
    with pytest.raises(TypeError) as err:
        sep_odd_eve([1,2,4,5,7,[8]])
        assert err.value.args[0] == "unsupported format, pass integers inside the list"
