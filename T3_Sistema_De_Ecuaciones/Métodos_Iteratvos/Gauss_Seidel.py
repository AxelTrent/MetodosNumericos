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
