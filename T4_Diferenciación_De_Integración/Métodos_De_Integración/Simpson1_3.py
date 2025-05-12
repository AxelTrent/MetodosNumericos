import math

def funcion(x):
    return x * math.sin(x)
def simpson13(a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser un número par")

    h = (b - a) / n
    suma = funcion(a) + funcion(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * funcion(x)
        else:
            suma += 4 * funcion(x)

    return (h / 3) * suma

# Parámetros
a = 0       # Límite inferior
b = 2       # Límite superior
n = 4       # Número de segmentos (par)

# Cálculo
resultado = simpson13(a, b, n)

# Resultados
print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método de Simpson 1/3: {resultado:.4g}")
