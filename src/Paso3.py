import numpy as np
from numpy.polynomial import Legendre
from utilidades import configurar_grafica
import matplotlib.pyplot as plt

def polinomios_legendre(x_vals):
    """
    Genera y grafica polinomios de Legendre
    """
    polinomios = [
        Legendre([1]),  
        Legendre([0, 1]),      
        Legendre([-0.5, 0, 1.5]) 
    ]
    
    configurar_grafica('Polinomios de Legendre')
    for i, p in enumerate(polinomios):
        y_vals = p(x_vals)
        plt.plot(x_vals, y_vals, label=f'P{i}(x)')
    plt.legend()
    plt.show()
    
    return polinomios