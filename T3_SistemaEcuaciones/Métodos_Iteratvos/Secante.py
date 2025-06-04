import math

def f(x):
    """Función de ejemplo: f(x) = x^2 - 4"""
    return x**2 - 4

def metodo_secante(x0, x1, tolerancia, max_iteraciones):
    """Implementa el método de la secante para encontrar una raíz de f(x)"""
    iteracion = 0
    print(f"{'Iteración':<10} {'x_n':<15} {'f(x_n)':<15} {'Error':<15}")
    
    while iteracion < max_iteraciones:
        # Calcular f(x0) y f(x1)
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Verificar si f(x1) - f(x0) es muy pequeño para evitar división por cero
        if abs(f_x1 - f_x0) < 1e-10:
            print("Error: La diferencia f(x1) - f(x0) es demasiado pequeña.")
            return None
        
        # Calcular el nuevo punto usando la fórmula del método de la secante
        x_nuevo = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Calcular el error
        error = abs(x_nuevo - x1)
        
        # Imprimir información de la iteración
        print(f"{iteracion:<10} {x_nuevo:<15.6f} {f(x_nuevo):<15.6f} {error:<15.6f}")
        
        # Verificar convergencia
        if error < tolerancia:
            print(f"\nConvergencia alcanzada en la iteración {iteracion + 1}!")
            print(f"Raíz aproximada: x = {x_nuevo:.6f}")
            return x_nuevo
        
        # Actualizar x0 y x1 para la siguiente iteración
        x0, x1 = x1, x_nuevo
        iteracion += 1
    
    print(f"\nAdvertencia: No se alcanzó convergencia dentro de {max_iteraciones} iteraciones.")
    return None

def main():
    print("Método de la Secante para encontrar una raíz de f(x)")
    x0 = float(input("Ingrese el primer punto inicial (x0): "))
    x1 = float(input("Ingrese el segundo punto inicial (x1): "))
    tolerancia = float(input("Ingrese la tolerancia deseada (por ejemplo, 0.00001): "))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones (por ejemplo, 100): "))
    
    raiz = metodo_secante(x0, x1, tolerancia, max_iteraciones)
    if raiz is not None:
        print(f"Solución final: x = {raiz:.6f}")
    else:
        print("No se encontró una raíz.")

if __name__ == "__main__":
    main()
