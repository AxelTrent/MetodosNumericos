import math

# Define la función a integrar
def funcion(x):
    return x * math.sin(x)

# Aplicación del método de Simpson 3/8
def simpson38(a, b, n):
    if n % 3 != 0:
        raise ValueError("n debe ser múltiplo de 3")

    h = (b - a) / n
    suma = funcion(a) + funcion(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            suma += 2 * funcion(x)
        else:
            suma += 3 * funcion(x)

    return (3 * h / 8) * suma

# Parámetros de integración
a = 0       # Límite inferior
b = 2       # Límite superior
n = 6       # Número de segmentos (múltiplo de 3)

# Cálculo de la integral
resultado = simpson38(a, b, n)

# Mostrar resultados
print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método de Simpson 3/8: {resultado:.4g}")
