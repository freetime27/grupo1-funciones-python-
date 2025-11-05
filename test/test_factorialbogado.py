#tests/test_factorial.py
from funciones.factorial import factorial
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-1)
    except ValueError:
        assert True
