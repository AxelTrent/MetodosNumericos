import math

def funcion(x):
    return x * math.sin(x)

def derivada_analitica(x):
    return math.sin(x) + x * math.cos(x)

def tres_puntos(x, h):
    fx1 = funcion(x + h)
    fx2 = funcion(x - h)
    return (fx1 - fx2) / (2 * h)
def main():
    x = 1
    h = 0.1

    derivada_numerica = tres_puntos(x, h)
    derivada_exacta = derivada_analitica(x)
    error_absoluto = abs(derivada_numerica - derivada_exacta)

    print("Función: f(x) = x * sin(x)")
    print(f"Punto de derivación: {x}")
    print(f"Tamaño del paso: {h}")
    print(f"Derivada numérica (Tres Puntos): {derivada_numerica:.6f}")
    print(f"Derivada analítica:               {derivada_exacta:.6f}")
    print(f"Error absoluto:                  {error_absoluto:.2e}")

if __name__ == "__main__":
    main()

