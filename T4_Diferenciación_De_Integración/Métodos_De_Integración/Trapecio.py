import math

# Define la función a integrar
def funcion(x):
    return x * math.sin(x)
# Método del Trapecio compuesto
def trapecio(a, b, n):
    h = (b - a) / n
    suma = (funcion(a) + funcion(b)) / 2

    for i in range(1, n):  # Solo del 1 al n-1
        x = a + i * h
        suma += funcion(x)
    
    return h * suma

# Parámetros de integración
a = 0       # Límite inferior
b = 2       # Límite superior
n = 4       # Número de segmentos
# Calcular la integral
resultado = trapecio(a, b, n)

# Imprimir resultados
print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método del Trapecio: {resultado:.4g}")
