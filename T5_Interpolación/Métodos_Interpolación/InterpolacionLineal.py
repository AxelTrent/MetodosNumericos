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
