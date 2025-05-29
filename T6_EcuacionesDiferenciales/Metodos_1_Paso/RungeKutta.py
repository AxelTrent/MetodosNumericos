import math

def evaluar_funcion(funcion, x, y):
    funcion = funcion.lower().replace(" ", "")

    funcion = funcion.replace("sin(x)", str(math.sin(x)))
    funcion = funcion.replace("cos(x)", str(math.cos(x)))
    funcion = funcion.replace("exp(x)", str(math.exp(x)))
    funcion = funcion.replace("log(x)", str(math.log(x)))

    funcion = funcion.replace("sin(y)", str(math.sin(y)))
    funcion = funcion.replace("cos(y)", str(math.cos(y)))
    funcion = funcion.replace("exp(y)", str(math.exp(y)))
    funcion = funcion.replace("log(y)", str(math.log(y)))

    funcion = funcion.replace("x", str(x))
    funcion = funcion.replace("y", str(y))

    return evaluar_expresion_simple(funcion)

def evaluar_expresion_simple(expr):
    resultado = 0
    expr = expr.replace("--", "+")
    sumandos = split_sumandos(expr)

    for sumando in sumandos:
        resultado += evaluar_producto(sumando)
    return resultado

def split_sumandos(expr):
    sumandos = []
    actual = ''
    for i, c in enumerate(expr):
        if c in '+-' and i != 0:
            sumandos.append(actual)
            actual = c
        else:
            actual += c
    sumandos.append(actual)
    return sumandos

def evaluar_producto(expr):
    if "/" in expr:
        factores = expr.split("/")
        resultado = evaluar_factor(factores[0])
        for f in factores[1:]:
            resultado /= evaluar_factor(f)
    elif "*" in expr:
        factores = expr.split("*")
        resultado = 1
        for f in factores:
            resultado *= evaluar_factor(f)
    else:
        resultado = evaluar_factor(expr)
    return resultado

def evaluar_factor(expr):
    expr = expr.strip()
    while expr.startswith("(") and expr.endswith(")"):
        expr = expr[1:-1].strip()
    while expr.startswith("+"):
        expr = expr[1:].strip()
    if expr == "":
        return 0
    try:
        return float(expr)
    except:
        print(f"Error al evaluar factor: {expr}")
        return 0
def runge_kutta(funcion, x0, y0, h, pasos):
    x = x0
    y = y0

    for i in range(pasos):
        k1 = h * evaluar_funcion(funcion, x, y)
        k2 = h * evaluar_funcion(funcion, x + h / 2.0, y + k1 / 2.0)
        k3 = h * evaluar_funcion(funcion, x + h / 2.0, y + k2 / 2.0)
        k4 = h * evaluar_funcion(funcion, x + h, y + k3)

        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        x += h

        print(f"Paso {i + 1}: x = {x:.5f}, y = {y:.5f}")
    return y

def main():
    print("Método Runge-Kutta sin eval(), funciones básicas")
    funcion = input("Ingresa la función f(x,y) (ej: x + y, sin(x) - y, x * y): ")
    x0 = float(input("Ingresa x0: "))
    y0 = float(input("Ingresa y0: "))
    h = float(input("Ingresa paso h: "))
    pasos = int(input("Número de pasos: "))

    resultado = runge_kutta(funcion, x0, y0, h, pasos)
    print(f"Resultado final: y({x0 + pasos * h:.5f}) = {resultado:.5f}")

if __name__ == "__main__":
    main()


