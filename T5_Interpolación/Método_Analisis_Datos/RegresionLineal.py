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
def calcular_error_absoluto(real, estimado):
    return abs(real - estimado)

def calcular_error_porcentual(valor_real, error_absoluto):
    return (error_absoluto / valor_real) * 100

def calcular_errores(x, y, pendiente, interseccion):
    n = len(x)
    suma_errores_porcentuales = 0.0

    print(" x\t y real\t y estimado\t Error abs\t Error %")
    print("-----------------------------------------------------")

    for i in range(n):
        # Calculamos el valor estimado
        y_estimado = pendiente * x[i] + interseccion
        
        # Calculamos errores
        error_abs = calcular_error_absoluto(y[i], y_estimado)
        error_porc = calcular_error_porcentual(y[i], error_abs)
        
        suma_errores_porcentuales += error_porc

        print(f"{x[i]:.1f}\t {y[i]:.1f}\t   {y_estimado:.2f}\t\t {error_abs:.2f}\t\t {error_porc:.2f}%")

    # Promedio del error porcentual
    promedio_error = suma_errores_porcentuales / n
    print(f"\nError Porcentual promedio: {promedio_error:.2f}%")

# En main():
    calcular_errores(x, y, m, b)
