import numpy as np
from utilidades import configurar_grafica
import matplotlib.pyplot as plt

def ajuste_minimos_cuadrados(x_data, y_data, x_vals, grado=2):
    """
    Implementa el ajuste por mínimos cuadrados
    """
    coeficientes = np.polyfit(x_data, y_data, grado)
    p = np.poly1d(coeficientes)
    y_ajustado = p(x_vals)
    
    configurar_grafica('Polinomio de Mínimos Cuadrados')
    plt.plot(x_data, y_data, 'ro', label='Datos experimentales')
    plt.plot(x_vals, y_ajustado, 'b-', label=f'Ajuste (grado {grado})')
    plt.legend()
    plt.show()
    
    return y_ajustado, coeficientes