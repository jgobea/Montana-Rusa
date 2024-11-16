import pytest
import numpy as np
from src.Paso3 import polinomios_legendre

def test_valores_polinomios_legendre():
    x_test = np.array([-1, -0.5, 0, 0.5, 1])
    polinomios = polinomios_legendre(x_test)

    p0_esperado = np.ones_like(x_test)
    assert np.allclose(polinomios[0](x_test), p0_esperado)
    

    p1_esperado = x_test
    assert np.allclose(polinomios[1](x_test), p1_esperado)
    

    p2_esperado = (3 * x_test**2 - 1) / 2
    assert np.allclose(polinomios[2](x_test), p2_esperado)