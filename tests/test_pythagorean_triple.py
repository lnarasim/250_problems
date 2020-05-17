import pytest
from pyproblems.pythagorean_triple import is_pythagorean_triple

def test_pythagorean_triple_valid():
    valid_triples = [(3, 4, 5), (5, 4, 3), (5, 12, 13), (36,77,85),
                    (35,612,613), (33,544,545), (37,684,685)]
    invalid_triples = [(1, 2, 3), (6, 7, 12), (200, 300, 500)]

    for triple in valid_triples:
        assert is_pythagorean_triple(triple)

    for triple in invalid_triples:
        assert not is_pythagorean_triple(triple)

def test_pythagorean_triple_invalid():
    invalid_triples = [(1, 2, 3), (6, 7, 12), (200, 300, 500)]

    for triple in invalid_triples:
        assert not is_pythagorean_triple(triple)

def test_pythagorean_triple_invalid_elements():
    invalid_triples = [(1, 2), (6), ()]

    for triple in invalid_triples:
        with pytest.raises(TypeError):
            is_pythagorean_triple(triple)

def test_pythagorean_triple_invalid_types():
    invalid_triples = [("123", "456", "789"), (6, "1", "3"), "123", None]

    for triple in invalid_triples:
        with pytest.raises(TypeError):
            is_pythagorean_triple(triple)