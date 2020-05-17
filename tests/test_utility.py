from pyproblems.utility import is_int
from pyproblems.utility import is_str

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