import unittest
import numpy as np
from src.Paso1 import trazador_cubico_sujeto
class TestTrazado (unittest.TestCase):
    
def test_trazador_cubico_parabola():
    x_data = np.array([0, 1, 2])
    y_data = np.array([0, 1, 4])
    x_test = np.array([0.5, 1.5])
    
    y_interpolado = trazador_cubico_sujeto(x_data, y_data, x_test)

    valores_esperados = np.array([0.25, 2.25])
    assert np.allclose(y_interpolado, valores_esperados, rtol=1e-2)

def test_trazador_cubico_seno():
    # Interpolación de función seno
    x_data = np.array([0, np.pi/2, np.pi])
    y_data = np.array([0, 1, 0])
    x_test = np.array([np.pi/4, 3*np.pi/4])
    
    y_interpolado = trazador_cubico_sujeto(x_data, y_data, x_test)
    
    valores_esperados = np.sin(x_test)
    assert np.allclose(y_interpolado, valores_esperados, rtol=1e-2)