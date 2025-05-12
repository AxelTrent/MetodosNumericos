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
 # Transformación de [-1,1] al intervalo [a,b]
    x1 = ((b - a) * t1 + (b + a)) / 2
    x2 = ((b - a) * t2 + (b + a)) / 2

    # Evaluar la función en los puntos transformados
    fx1 = funcion(x1)
    fx2 = funcion(x2)

    # Aplicar la fórmula de cuadratura
    return (b - a) / 2 * (w * fx1 + w * fx2)

# Parámetros
a = 0       # Límite inferior
b = 2       # Límite superior
n = 4       # Número de segmentos (no se usa en 2 puntos)

# Calcular la integral
resultado = cuadratura_gaussiana(a, b)

# Imprimir resultados
print("Función: x * sin(x)")
print(f"Límite Inferior: {a}")
print(f"Límite Superior: {b}")
print(f"Número de Segmentos: {n} (no aplicable directamente en Gauss 2 puntos)")
print(f"Resultado de la Integral por el método de Cuadratura Gaussiana: {resultado:.4g}")
