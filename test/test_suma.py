#tests/test_sumar.py
from funciones.suma import sumar
def test_sumar():
 assert sumar(3, 5) == 8
 assert sumar(-2, 2) == 0
