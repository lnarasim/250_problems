from pyproblems.word_count import word_count
import pytest

def test_word_count_valid():
    assert word_count("1 2 3") == {"1": 1, "2": 1, "3": 1}
    assert word_count("123 456 789") == {"123": 1, "456": 1, "789": 1}
    assert word_count("welcome to python land python land") == {"welcome": 1, "to": 1, 
                                                    "python": 2, "land": 2}
    assert word_count("tik tik tik") == {"tik": 3}
    assert word_count("") == {}
    assert word_count("123") == {"123": 1}

def test_word_count_invalid():
    invalid_inputs = [123, 10.1, [1, 2, 3, 4], {1: 1, 2: 2}, None, True]

    for obj in invalid_inputs:
        with pytest.raises(TypeError):
            word_count(obj)