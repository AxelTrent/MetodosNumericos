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

    tolerancia = float(input("Ingrese la tolerancia adecuada (de preferencia 0.000001): "))
    max_iteraciones = int(input("Ingrese el número máximo de Iteraciones (Por ejemplo, 100): "))

    for i in range(n):
        x[i] = 0
        anterior[i] = 0

   print("\nIniciando Iteraciones de Gauss - Seidel")
    iteracion = 0

    while iteracion < max_iteraciones:
        for i in range(n):
            anterior[i] = x[i]

        for i in range(n):
            suma = soluciones[i]
            for j in range(n):
                if j != i:
                    suma -= matriz[i][j] * x[j]
            x[i] = suma / matriz[i][i]

        print(f"Iteración {iteracion + 1}:")
        for j in range(n):
            print(f"x[{j}] = {x[j]:.3f}")

        convergencia = True
        for j in range(n):
            if abs(x[j] - anterior[j]) > tolerancia:
                convergencia = False
                break

        if convergencia:
            print("\nConvergencia alcanzada")
            print("Solución Final:")
            for j in range(n):
                print(f"x[{j}] = {x[j]:.3f}")
            break

        iteracion += 1

    if iteracion >= max_iteraciones:
        print("\nNo se alcanzó convergencia dentro del número máximo de iteraciones")

if __name__ == "__main__":
    main()
