from funciones.dividir_olguin import dividir_olguin

def test_dividir_olguin():
    assert dividir_olguin(10, 2) == 5
    assert dividir_olguin(5, 0) is None
