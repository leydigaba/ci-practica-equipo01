import pytest
from calculadora import suma, resta, multiplicacion, division, potencia

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(10, 4) == 6

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(10, 2) == 5
    with pytest.raises(ValueError):
        division(5, 0)

def test_potencia():
    assert potencia(2, 3) == 8