import pytest
import numpy as np
from src.Paso2 import ajuste_minimos_cuadrados

def test_minimos_cuadrados_lineal():
    # Caso lineal perfecto: y = 2x + 1
    x_data = np.array([0, 1, 2, 3])
    y_data = np.array([1, 3, 5, 7])
    x_test = np.array([0.5, 1.5, 2.5])
    
    y_ajustado, coeficientes = ajuste_minimos_cuadrados(x_data, y_data, x_test, grado=1)
    
    # Verificar coeficientes 
    assert np.allclose(coeficientes, [2, 1], rtol=1e-10)
    
    # Verificar valores ajustados
    valores_esperados = 2 * x_test + 1
    assert np.allclose(y_ajustado, valores_esperados, rtol=1e-10)

def test_minimos_cuadrados_cuadratico():
    # Caso cuadrático
    x_data = np.array([-1, 0, 1, 2])
    y_data = np.array([4, 1, 0, 1])
    x_test = np.array([0.5, 1.5])
    
    y_ajustado, coeficientes = ajuste_minimos_cuadrados(x_data, y_data, x_test, grado=2)
    
    # Verificar coeficientes 
    assert np.allclose(coeficientes, [1, -2, 1], rtol=1e-10)
    
    # Verificar valores ajustados
    valores_esperados = x_test**2 - 2*x_test + 1
    assert np.allclose(y_ajustado, valores_esperados, rtol=1e-10) 