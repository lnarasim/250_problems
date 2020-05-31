from pyproblems.area import area
import pytest

def test_find_area():
    assert area(10) == 100
    assert area(10,5) == 50
    assert area(5,2) == 10
    assert area(1.2,1.2) == 1.44
    assert area(37,14) == 518
    assert area(0.15) == 0.0225

def test_unsupported():
    with pytest.raises(ValueError):
        area(4,2,5) #Too many arguments for breadth

    with pytest.raises(ValueError):
        area(4,0) #Breadth as 0
    
    with pytest.raises(ValueError):
        area(0,5) #Length as 0

    with pytest.raises(ValueError):
        area(0) #length as 0

    with pytest.raises(TypeError):
        area('4',2) #Length as string

    with pytest.raises(TypeError):
        area(4,[2,5]) #Var Positional as list

    with pytest.raises(TypeError):
        area(4,(2,)) #Var Positional as tuple