import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def configurar_grafica(titulo):
    """
    Configura el formato de la gráfica
    """
    plt.figure(figsize=(10, 6))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')

def cargar_datos(nombre_archivo):
    """
    Carga datos desde un archivo CSV
    """
    try:
        datos = pd.read_csv(nombre_archivo)
        if 'x' not in datos.columns or 'y' not in datos.columns:
            print(f"Error: El archivo {nombre_archivo} debe contener columnas 'x' y 'y'")
            return None, None
        return datos['x'].values, datos['y'].values
    except Exception as e:
        print(f"Error al cargar {nombre_archivo}: {e}")
        return None, None

def cargar_sistema_ecuaciones(nombre_archivo):
    """
    Carga el sistema de ecuaciones desde CSV
    """
    try:
        datos = np.loadtxt(nombre_archivo, delimiter=',')
        if datos.shape[1] < 2:
            print(f"Error: El archivo {nombre_archivo} debe contener al menos dos columnas")
            return None, None
        A = datos[:, :-1]
        b = datos[:, -1]
        return A, b
    except Exception as e:
        print(f"Error al cargar sistema de ecuaciones: {e}")
        return None, None