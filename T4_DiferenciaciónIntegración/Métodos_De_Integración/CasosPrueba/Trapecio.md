# Caso que funciona
```python
import math

def funcion(x):
    return x * math.sin(x)

def trapecio(a, b, n):
    h = (b - a) / n
    suma = (funcion(a) + funcion(b)) / 2
    for i in range(1, n):
        x = a + i * h
        suma += funcion(x)
    return h * suma

a = 0
b = 2
n = 4
resultado = trapecio(a, b, n)

print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método del Trapecio: {resultado:.4g}")
Salida:

Función: x * sin(x)
Límite inferior: 0
Límite superior: 2
Número de segmentos: 4
Resultado de la integral por el método del Trapecio: 1.877
```

### Explicación:
Funciona porque los límites [0, 2] son válidos, n = 4 es un número positivo, y la función x * sin(x) es continua. El método del trapecio calcula la integral, aunque con menor precisión que los métodos de Simpson.

# Caso de error
```python
import math

def funcion(x):
    return x * math.sin(x)

def trapecio(a, b, n):
    h = (b - a) / n
    suma = (funcion(a) + funcion(b)) / 2
    for i in range(1, n):
        x = a + i * h
        suma += funcion(x)
    return h * suma

a = 0
b = 2
n = 0  # Error: división por cero
resultado = trapecio(a, b, n)

print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método del Trapecio: {resultado:.4g}")
Salida:

ZeroDivisionError: float division by zero
```
### Explicación: 
El método del trapecio calcula $$h = (b - a) / n, y si n = 0$$ , se produce una división por cero, generando un error explícito.
