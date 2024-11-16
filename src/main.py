import numpy as np
from utilidades import cargar_datos, cargar_sistema_ecuaciones
from Paso1 import trazador_cubico_sujeto
from Paso2 import ajuste_minimos_cuadrados
from Paso3 import polinomios_legendre
from Paso4 import resolver_sistema_ecuaciones

def main():
    # Paso 1: Trazador Cúbico
    print("Cargando datos para el trazador cúbico...")
    x_datos_spline, y_datos_spline = cargar_datos('Paso1.csv')
    
    if x_datos_spline is not None:
        x_vals_spline = np.linspace(min(x_datos_spline), max(x_datos_spline), 100)
        y_interpolado = trazador_cubico_sujeto(x_datos_spline, y_datos_spline, x_vals_spline)
        print("Interpolación completada.")
    
    # Paso 2: Mínimos Cuadrados
    print("\nCargando datos para mínimos cuadrados...")
    x_datos_mc, y_datos_mc = cargar_datos('Paso2.csv')
    
    if x_datos_mc is not None:
        x_vals_mc = np.linspace(min(x_datos_mc), max(x_datos_mc), 100)
        y_ajustado, coeficientes = ajuste_minimos_cuadrados(x_datos_mc, y_datos_mc, x_vals_mc)
        print("Coeficientes del polinomio ajustado:", coeficientes)
    
    # Paso 3: Polinomios Ortogonales
    print("\nGenerando polinomios ortogonales...")
    x_vals_legendre = np.linspace(-1, 1, 100)
    polinomios = polinomios_legendre(x_vals_legendre)
    
    # Paso 4: Sistema de Ecuaciones
    print("\nResolviendo sistema de ecuaciones...")
    A, b = cargar_sistema_ecuaciones('Paso4.csv')
    
    if A is not None and b is not None:
        solucion = resolver_sistema_ecuaciones(A, b)
        if solucion is not None:
            print("\nSolución del sistema de ecuaciones:")
            for i, sol in enumerate(solucion):
                print(f"x{i+1} = {sol:.4f}")

if __name__ == "__main__":
    main()