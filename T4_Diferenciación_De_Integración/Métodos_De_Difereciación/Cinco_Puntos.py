import math

def funcion(x):
    return x * math.sin(x)

def cinco_puntos(x, h):
    # Evaluar la función en los puntos necesarios
    fx1 = funcion(x + 2 * h)
    fx2 = funcion(x + h)
    fx3 = funcion(x - h)
    fx4 = funcion(x - 2 * h)
     # Aplicar la fórmula de los Cinco Puntos
    return (-fx1 + 8 * fx2 - 8 * fx3 + fx4) / (12 * h)

def main():
    # Definir parámetros fijos
    x = 1
    h = 0.1

    resultado = cinco_puntos(x, h)
 # Imprimir resultados
    print("Función: x * sin(x)")
    print(f"Punto de Derivación: {x}")
    print(f"Resultado de la Derivada por el método de los Cinco Puntos: {resultado:.4g}")

if __name__ == "__main__":
    main()
