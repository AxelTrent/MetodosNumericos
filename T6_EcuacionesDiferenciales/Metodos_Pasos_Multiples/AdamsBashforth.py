import math

# Función que define la ecuación diferencial dy/dx = f(x, y)
def f(x, y):
    return -2 * x * y  # puedes cambiarla si deseas otra ecuación

# Método principal de Adams-Bashforth
def adams_bashforth(x0, y0, xf, h):
    n = int(math.ceil((xf - x0) / h))
    x = [0.0] * (n + 1)
    y = [0.0] * (n + 1)
    f_vals = [0.0] * (n + 1)

    x[0] = x0
    y[0] = y0
    f_vals[0] = f(x[0], y[0])

    # Runge-Kutta para los primeros 3 puntos
    for i in range(3):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + (h * k1)/2)
        k3 = f(x[i] + h/2, y[i] + (h * k2)/2)
        k4 = f(x[i] + h, y[i] + h * k3)

        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        f_vals[i + 1] = f(x[i + 1], y[i + 1])

    # Imprimimos los primeros resultados
    print(f"{'x':>10} {'y':>10}")
    for i in range(4):
        print(f"{x[i]:10.4f} {y[i]:10.4f}")

    # Adams-Bashforth orden 4 para los siguientes pasos
    for i in range(3, n):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + (h/24) * (
            55 * f_vals[i] - 59 * f_vals[i-1] + 37 * f_vals[i-2] - 9 * f_vals[i-3]
        )
        f_vals[i + 1] = f(x[i + 1], y[i + 1])

        print(f"{x[i + 1]:10.4f} {y[i + 1]:10.4f}")

# Función principal que pide datos al usuario
def main():
    print("Método de Adams-Bashforth de orden 4")
    x0 = float(input("Ingresa el valor inicial de x (x0): "))
    y0 = float(input("Ingresa el valor inicial de y (y0): "))
    xf = float(input("Ingresa el valor final de x (xf): "))
    h = float(input("Ingresa el tamaño del paso (h): "))

    adams_bashforth(x0, y0, xf, h)

if __name__ == "__main__":
    main()

