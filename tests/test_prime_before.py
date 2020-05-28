from pyproblems.prime_before import prime_before
import pytest

def test_prime_before_number():
    assert prime_before(5) == 3
    assert prime_before(10) == 7
    assert prime_before(100) == 97
    assert prime_before(497) == 491
    assert prime_before(9457) == 9439

def test_prime_before_invalid():
    with pytest.raises(TypeError):
        prime_before(True)

    with pytest.raises(TypeError):
        prime_before(None)

    with pytest.raises(TypeError):
        prime_before((91,))

    with pytest.raises(TypeError):
        prime_before([90])

    with pytest.raises(TypeError):
        prime_before(10.0)

    with pytest.raises(ValueError):
        prime_before(0)

    with pytest.raises(ValueError):
        prime_before(1)

    with pytest.raises(ValueError):
        prime_before(2)

    with pytest.raises(ValueError):
        prime_before(-5)