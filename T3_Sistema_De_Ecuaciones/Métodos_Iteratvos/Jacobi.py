
def main():
    n = int(input("Ingrese el número de ecuaciones (n): "))

    matriz = [[0.0 for _ in range(n)] for _ in range(n)]
    soluciones = [0.0 for _ in range(n)]
    x = [0.0 for _ in range(n)]
    anterior = [0.0 for _ in range(n)]

    print("Ingrese la matriz aumentada (coeficientes y términos independientes):")
    for i in range(n):
        print(f"Ecuación {i + 1}:")
        for j in range(n):
            matriz[i][j] = float(input(f"Coeficiente [{i + 1}][{j + 1}]: "))
        soluciones[i] = float(input(f"Término Independiente [{i + 1}]: "))

 # Validar elementos diagonales
    for i in range(n):
        if abs(matriz[i][i]) < 1e-10:
            print(f"Error: El elemento diagonal matriz[{i}][{i + 1}] es cero o muy pequeño.")
            return

    tolerancia = float(input("Ingrese la tolerancia deseada (Por ejemplo: 0.00001): "))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones (Por ejemplo: 100): "))

    for i in range(n):
        x[i] = 0
        anterior[i] = 0

 print("\nIniciando iteraciones de Jacobi....")
    iteracion = 0

    while iteracion < max_iteraciones:
        iteracion += 1

        for i in range(n):
            suma = soluciones[i]
            for j in range(n):
                if j != i:
                    suma -= matriz[i][j] * anterior[j]
            x[i] = suma / matriz[i][i]

        max_diferencia = max(abs(x[i] - anterior[i]) for i in range(n))

        print(f"Iteración {iteracion} (Diferencia Máxima: {max_diferencia:.3f}):")
        for i in range(n):
            print(f"x[{i}] = {x[i]:.3f}")
# Verificar convergencia
        if all(abs(x[i] - anterior[i]) <= tolerancia for i in range(n)):
            print(f"\nConvergencia alcanzada en la iteración {iteracion}!")
            break

        # Copiar valores a 'anterior' para la siguiente iteración
        for i in range(n):
            anterior[i] = x[i]

    if iteracion >= max_iteraciones:
        print("\nAdvertencia: No se alcanzó convergencia dentro del número de iteraciones establecidas")

    print("\nSolución Final:")
    for i in range(n):
        print(f"x[{i}] = {x[i]:.3f}")

if __name__ == "__main__":
    main()
