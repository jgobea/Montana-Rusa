import numpy as np
from scipy.interpolate import CubicSpline
from utilidades import configurar_grafica
import matplotlib.pyplot as plt

def trazador_cubico_sujeto(x_data, y_data, x_vals):
    """
    Implementa el método de trazador cúbico sujeto
    """
    cs = CubicSpline(x_data, y_data)
    y_interpolado = cs(x_vals)
    
    configurar_grafica('Trazador Cúbico Sujeto')
    plt.plot(x_data, y_data, 'ro', label='Puntos de control')
    plt.plot(x_vals, y_interpolado, 'b-', label='Spline cúbico')
    plt.legend()
    plt.show()
    
    return y_interpolado