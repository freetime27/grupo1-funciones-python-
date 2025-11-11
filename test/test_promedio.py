#test/test_promedio.py
from funciones.promedioolmedo import promedio
def test_promedio():
 assert promedio([2, 4, 6]) == 4
 assert promedio([]) is None
