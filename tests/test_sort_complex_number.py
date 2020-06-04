from pyproblems.complex_number_sorter import sort_complex_numbers
import pytest

def test_sort_complex_number():
    assert sort_complex_numbers(4+5j, 5+8j,3j,4) == (3j,  (4+5j), 4, (5+8j))
    assert sort_complex_numbers(1,2,4,5) == (1,2,4,5)
    assert sort_complex_numbers(1+4j,2j,4.5 + 3j,5j) == (2j,5j,1+4j,4.5+3j)
    assert sort_complex_numbers(1+2j,1.5+9j,2.5+7j,2+4j,1+8j) == (1+2j,1+8j,1.5+9j,2+4j,2.5+7j)
    assert sort_complex_numbers(-1-2j,4-5j,3j) == (-1-2j,3j,4-5j)
    assert sort_complex_numbers() == ()

def test_sort_complex_number_errors_1():
    with pytest.raises(TypeError):
        sort_complex_numbers(True,5+8j,3j,4)

def test_sort_complex_number_errors_2():
    with pytest.raises(TypeError):
        sort_complex_numbers(False,5+8j,-2+3j,4-6j)

def test_sort_complex_number_errors_3():
    with pytest.raises(TypeError):
        sort_complex_numbers([True,5+8j,3j,4])

def test_sort_complex_number_errors_4():
    with pytest.raises(TypeError):
        sort_complex_numbers((1+2j,1.5+9j),[2.5+7j,2+4j],1+8j)

def test_sort_complex_number_errors_5():
    with pytest.raises(TypeError):
        sort_complex_numbers({-1-2j,4-5j,3j})  
        