from funciones.potencia_peveri import potencia_peveri

def test_potencia_peveri():
    assert potencia_peveri(2, 3) == 8
    assert potencia_peveri(5, 0) == 1
