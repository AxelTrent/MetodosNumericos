import math

def mostrar_datos(x, y):
    print(" x\t y")
    print("-----------")
    for i in range(len(x)):
        print(f"{x[i]:.1f}\t{y[i]:.1f}")
    print()

def main():
    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 6]
    
    # Mostrar datos en formato tabla
    mostrar_datos(x, y)
