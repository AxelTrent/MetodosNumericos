
# Newton-Raphson.py
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces.
    f: función
    df: derivada de la función
    x0: valor inicial
    tol: tolerancia
    max_iter: número máximo de iteraciones
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivada igual a cero, método falla.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    raise ValueError("No convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: f(x) = x^2 - 2
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    x0 = 1.0
    raiz, iteraciones = newton_raphson(f, df, x0)
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones: {iteraciones}")
