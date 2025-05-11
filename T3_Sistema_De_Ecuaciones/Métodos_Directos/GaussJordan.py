def mostrar_matriz(matriz, soluciones, n):
    for i in range(n):
        print("| ", end="")
        for j in range(n):
            print(f"{matriz[i][j]:8.3f} ", end="")
        print(f"| {soluciones[i]:8.3f} |")
    print()
    
def main():
    
    # Leer número de ecuaciones
    n = int(input("Introduce el número de ecuaciones (n): "))

    matriz = [[0.0 for _ in range(n)] for _ in range(n)]
    soluciones = [0.0 for _ in range(n)]
    x = [0.0 for _ in range(n)]
    
 # Leer matriz aumentada
    print("Ingrese la matriz aumentada (coeficientes y términos independientes):")
    for i in range(n):
        print(f"Ecuación {i + 1}:")
        for j in range(n):
            matriz[i][j] = float(input(f"Coeficiente [{i + 1}][{j + 1}]: "))
        soluciones[i] = float(input(f"Término independiente [{i + 1}]: "))

    print("\nMatriz aumentada ingresada:")
    mostrar_matriz(matriz, soluciones, n)
