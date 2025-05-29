# Metodo_de_Regla_Falsa.py
def regla_falsa(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Regla Falsa para encontrar raíces.
    f: función
    a, b: límites del intervalo [a, b]
    tol: tolerancia
    max_iter: número máximo de iteraciones
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos.")
    
    for i in range(max_iter):
        fa, fb = f(a), f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol or abs(b - a) < tol:
            return c, i + 1
        if fa * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("No convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: f(x) = x^3 - x - 2
    f = lambda x: x**3 - x - 2
    a, b = 1, 2
    raiz, iteraciones = regla_falsa(f, a, b)
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones: {iteraciones}")
