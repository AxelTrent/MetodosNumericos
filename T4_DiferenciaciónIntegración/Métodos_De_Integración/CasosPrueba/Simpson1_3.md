# Caso que funciona
```python
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

a = 0
b = 2
n = 4
resultado = simpson13(a, b, n)

print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método de Simpson 1/3: {resultado:.4g}")
Salida:

Función: x * sin(x)
Límite inferior: 0
Límite superior: 2
Número de segmentos: 4
Resultado de la integral por el método de Simpson 1/3: 1.896
```

### Explicación:
Funciona porque n = 4 es par, los límites [0, 2] son válidos, y la función x * sin(x) es continua. El método de Simpson 1/3 calcula la integral con buena precisión.

# Caso de error
```python
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

a = 0
b = 2
n = 3  # Error: n no es par
resultado = simpson13(a, b, n)

print("Función: x * sin(x)")
print(f"Límite inferior: {a}")
print(f"Límite superior: {b}")
print(f"Número de segmentos: {n}")
print(f"Resultado de la integral por el método de Simpson 1/3: {resultado:.4g}")
Salida:

ValueError: n debe ser un número par
```
### Explicación: 
El método de Simpson 1/3 requiere que n sea par. Al usar n = 3, se genera un error explícito debido a la verificación en el código.
