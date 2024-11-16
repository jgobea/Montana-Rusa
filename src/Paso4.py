from scipy.linalg import solve
import numpy as np

def resolver_sistema_ecuaciones(A, b):
    """
    Resuelve el sistema de ecuaciones lineales Ax = b

    """
    try:
        # Verificar que la matriz A es cuadrada
        if A.shape[0] != A.shape[1]:
            print("Error: La matriz A debe ser cuadrada")
            return None
            
        # Verificar que las dimensiones son compatibles
        if A.shape[0] != len(b):
            print("Error: Dimensiones incompatibles entre A y b")
            return None
            
        solucion = solve(A, b)
        return solucion
        
    except np.linalg.LinAlgError:
        print("Error: El sistema no tiene solución única (matriz singular)")
        return None
    except Exception as e:
        print(f"Error al resolver el sistema: {e}")
        return None