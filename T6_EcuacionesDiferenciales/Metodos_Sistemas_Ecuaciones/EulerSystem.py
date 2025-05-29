import math

def f(x, y1, y2):
    # Define el sistema de ecuaciones diferenciales
    # dy1/dx = -2xy1
    # dy2/dx = y1 - y2
    dy1 = -2 * x * y1
    dy2 = y1 - y2
    return [dy1, dy2]

def euler_method(x0, y1_0, y2_0, xf, h):
    # Cálculo del número de pasos
    n = int(math.ceil((xf - x0) / h))
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    # Valores iniciales
    x[0] = x0
    y1[0] = y1_0
    y2[0] = y2_0

    # Encabezado
    print(f"{'x':>10} {'y1':>10} {'y2':>10}")
    print(f"{x[0]:10.4f} {y1[0]:10.4f} {y2[0]:10.4f}")

    # Método de Euler
    for i in range(n):
        dx1, dx2 = f(x[i], y1[i], y2[i])
        x[i + 1] = x[i] + h
        y1[i + 1] = y1[i] + h * dx1
        y2[i + 1] = y2[i] + h * dx2
        print(f"{x[i + 1]:10.4f} {y1[i + 1]:10.4f} {y2[i + 1]:10.4f}")

def main():
    print("Método de Euler para un sistema de 2 ecuaciones diferenciales")
    x0 = float(input("Ingresa el valor inicial de x (x0): "))
    y1_0 = float(input("Ingresa el valor inicial de y1 (y1_0): "))
    y2_0 = float(input("Ingresa el valor inicial de y2 (y2_0): "))
    xf = float(input("Ingresa el valor final de x (xf): "))
    h = float(input("Ingresa el tamaño del paso (h): "))

    euler_method(x0, y1_0, y2_0, xf, h)

if __name__ == "__main__":
    main()
