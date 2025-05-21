import math

def main():
    # Puntos conocidos en x, y
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    print("Puntos Utilizados:")
    for i in range(len(x)):
        print(f"x = {x[i]:.1f}, y = {y[i]:.1f}")

def calcular_correlacion(x, y):
    n = len(x)
    suma_x = suma_y = suma_xy = suma_x2 = suma_y2 = 0.0

    for i in range(n):
        suma_x += x[i]
        suma_y += y[i]
        suma_xy += x[i] * y[i]
        suma_x2 += x[i] ** 2
        suma_y2 += y[i] ** 2

    numerador = n * suma_xy - suma_x * suma_y
    denominador = math.sqrt((n * suma_x2 - suma_x ** 2) * (n * suma_y2 - suma_y ** 2))

    return numerador / denominador if denominador != 0 else 0

# En main():
r = calcular_correlacion(x, y)
print(f"\nCoeficiente de correlación: {r:.4f}")
