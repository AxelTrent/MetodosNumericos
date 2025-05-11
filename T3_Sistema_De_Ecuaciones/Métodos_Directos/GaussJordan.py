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
