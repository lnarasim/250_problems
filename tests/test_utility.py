from pyproblems.utility import is_int
from pyproblems.utility import is_str
from pyproblems.utility import is_float

def test_is_int():
    assert is_int(10) == True
    assert is_int(10.1) == False
    assert is_int("10") == False
    assert is_int([1, 2, 3]) == False
    assert is_int((1, 2, 3)) == False
    assert is_int({1: 2, 2: 2}) == False
    assert is_int(True) == False
    assert is_int(None) == False
    assert is_int(set()) == False
    assert is_int(1000) == True
    assert is_int(10000000) == True
    assert is_int(1)
    
def test_is_str():
    assert is_str("123")
    assert is_str("hello")
    assert is_str("""123""")
    assert is_str("10")
    assert is_str(10.1) == False    
    assert is_str([1, 2, 3]) == False
    assert is_str((1, 2, 3)) == False
    assert is_str({1: 2, 2: 2}) == False
    assert is_str(True) == False
    assert is_str(None) == False
    assert is_str(set()) == False
    assert is_str(1000) == False

def test_is_float():
    assert is_float(1.0)
    assert not is_float(10)
    assert not is_float(True)
    assert not is_float(False)
    assert is_float(10.000000054)
    assert not is_float("10.4")
    assert is_float(10.4)
    assert not is_float((14.5,2.0))

