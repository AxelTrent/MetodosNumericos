def mostrar_matriz(matriz, soluciones, n):
    for i in range(n):
        print("|", end="")
        for j in range(n):
            print(f"{matriz[i][j]:8.3f} ", end="")
        print(f"| {soluciones[i]:8.3f}|")
    print()

def main():
    # Leer tamaño de la matriz
    n = int(input("Ingrese el número de ecuaciones (n): "))

    matriz = [[0.0 for _ in range(n)] for _ in range(n)]
    soluciones = [0.0 for _ in range(n)]
    x = [0.0 for _ in range(n)]

    print("Ingrese la matriz aumentada (coeficientes y términos independientes):")
    for i in range(n):
        print(f"Ecuación {i + 1}:")
        for j in range(n):
            matriz[i][j] = float(input(f"Coeficiente [{i + 1}][{j + 1}]: "))
        soluciones[i] = float(input(f"Término independiente [{i + 1}]: "))

    print("\nMatriz Aumentada Ingresada")
    mostrar_matriz(matriz, soluciones, n)

    # Eliminación Gaussiana
    for j in range(n):
        for i in range(j + 1, n):
            factor = matriz[i][j] / matriz[j][j]
            for k in range(n):
                matriz[i][k] -= factor * matriz[j][k]
            soluciones[i] -= factor * soluciones[j]
            print(f"\nEliminando elemento [{i + 1}][{j + 1}] con factor {factor:.3f}:")
            mostrar_matriz(matriz, soluciones, n)

    # Sustitución hacia atrás
    print("\nResolviendo por sustitución hacia atrás")
    for i in range(n - 1, -1, -1):
        suma = sum(matriz[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (soluciones[i] - suma) / matriz[i][i]
        print(f"x[{i}] = {x[i]:.3f}")

    # Mostrar solución final
    print("\nSolución Final:")
    for i in range(n):
        print(f"x[{i}] = {x[i]:.3f}")

if __name__ == "__main__":
    main()

