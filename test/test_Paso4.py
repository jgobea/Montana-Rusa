import pytest
import numpy as np
from src.Paso4 import resolver_sistema_ecuaciones

def test_sistema_2x2():
    # Sistema simple 2x2:

    A = np.array([[2, 1],
                  [1, 3]])
    b = np.array([5, 6])
    solucion = resolver_sistema_ecuaciones(A, b)
    
    esperado = np.array([1.7857142857142858, 1.4285714285714286])
    assert np.allclose(solucion, esperado)

def test_sistema_3x3():
    # Sistema 3x3:

    A = np.array([[1, 1, 1],
                  [2, -1, 1],
                  [1, 2, -1]])
    b = np.array([6, 2, 1])
    solucion = resolver_sistema_ecuaciones(A, b)
    
    esperado = np.array([1., 2., 3.])
    assert np.allclose(solucion, esperado)

@pytest.mark.parametrize("A,b,esperado", [
    (np.eye(3), np.array([1, 2, 3]), np.array([1, 2, 3])),
    (np.array([[0, 1], [-1, 0]]), np.array([1, 0]), np.array([0, 1]))
])
def test_casos_especiales(A, b, esperado):
    solucion = resolver_sistema_ecuaciones(A, b)
    assert np.allclose(solucion, esperado) 