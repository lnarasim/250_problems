from pyproblems.perfect_number import perfect_num
import pytest

def test_perfnum_1():
    n = 28
    ret_val = perfect_num(n)
    assert ret_val == True

def test_perfnum_2():
    n = 6,28,496
    for i in n:
        ret_val = perfect_num(i)
        assert ret_val == True

def test_not_perfnum_1():
    n = 11
    ret_val = perfect_num(n)
    assert ret_val == False

def test_not_perfnum_2():
    n = 1
    ret_val = perfect_num(n)
    assert ret_val == False

def test_bool_perfnum():
    n = True
    with pytest.raises(TypeError) as err:
        perfect_num(n)
        assert err.value.args[0] == "unsupported format"

def test_other_perfnum():
    n = [1,2,3]
    with pytest.raises(TypeError) as err:
        perfect_num(n)
        assert err.value.args[0] == "unsupported format"