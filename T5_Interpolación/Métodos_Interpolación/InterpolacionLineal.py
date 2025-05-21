def mostrar_puntos_utilizados(x0, y0, x1, y1):
    """Muestra los puntos conocidos que se usarán para la interpolación"""
    print("\nPuntos Utilizados:")
    print(f"x0 = {x0:.1f}, y0 = {y0:.1f}")
    print(f"x1 = {x1:.1f}, y1 = {y1:.1f}")

# Datos iniciales
x0, y0 = 2, 4    # Primer punto conocido
x1, y1 = 4, 16   # Segundo punto conocido
x_buscado = 3    # Punto a interpolar
valor_real = 9   # Valor real (para comparación)

# Mostrar configuración inicial
print("=== CONFIGURACIÓN INICIAL ===")
print(f"Buscando valor en x = {x_buscado}")
mostrar_puntos_utilizados(x0, y0, x1, y1)
def interpolar_linealmente(x0, y0, x1, y1, x):
    """Realiza la interpolación lineal entre dos puntos"""
    # Fórmula: y = y0 + (y1-y0)/(x1-x0) * (x-x0)
    pendiente = (y1 - y0) / (x1 - x0)
    return y0 + pendiente * (x - x0)

# Realizar interpolación
print("\n=== CÁLCULO DE INTERPOLACIÓN ===")
resultado = interpolar_linealmente(x0, y0, x1, y1, x_buscado)
print(f"Valor interpolado en x = {x_buscado:.1f}: {resultado:.4f}")
def calcular_error_absoluto(real, estimado):
    """Calcula la diferencia absoluta entre valor real y estimado"""
    return abs(real - estimado)

def calcular_error_porcentual(real, estimado):
    """Calcula el error porcentual respecto al valor real"""
    return (abs(real - estimado) / real) * 100

# Calcular y mostrar errores
print("\n=== ANÁLISIS DE ERRORES ===")
error_abs = calcular_error_absoluto(valor_real, resultado)
error_porc = calcular_error_porcentual(valor_real, resultado)

print(f"Valor real: {valor_real}")
print(f"Valor interpolado: {resultado:.4f}")
print(f"Error Absoluto: {error_abs:.4f}")
print(f"Error Porcentual: {error_porc:.2f}%")
