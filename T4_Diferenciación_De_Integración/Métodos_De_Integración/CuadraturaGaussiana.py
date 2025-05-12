import math

# Define la función a integrar
def funcion(x):
    return x * math.sin(x)

# Método de Cuadratura Gaussiana con 2 puntos
def cuadratura_gaussiana(a, b):
    # Puntos y pesos para 2 puntos de Gauss-Legendre
    t1 = -0.577350269  # Primer punto
    t2 =  0.577350269  # Segundo punto
    w = 1.0            # Peso igual para ambos
