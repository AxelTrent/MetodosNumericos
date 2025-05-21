def mostrar_datos(x, y):
    print(" x\t y")
    print("------------")
    for i in range(len(x)):
        print(f"{x[i]:.1f}\t{y[i]:.1f}")
    print()

def main():
    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 6]
    
    # Mostrar datos en formato tabla
    mostrar_datos(x, y)
def calcular_regresion_lineal(x, y):
    n = len(x)
    suma_x = suma_y = suma_xy = suma_x2 = 0.0

    for i in range(n):
        suma_x += x[i]
        suma_y += y[i]
        suma_xy += x[i] * y[i]
        suma_x2 += x[i] ** 2

    # Fórmulas para pendiente (m) e intersección (b)
    pendiente = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
    interseccion = (suma_y - pendiente * suma_x) / n
    
    return pendiente, interseccion

# En main():
    m, b = calcular_regresion_lineal(x, y)
    print(f"Ecuación ajustada: y = {m:.4f}x + {b:.4f}\n")
