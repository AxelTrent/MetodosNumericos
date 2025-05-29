# Punto-Fijo.py
def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    """
    Método de Punto Fijo para encontrar raíces.
    g: función g(x) tal que x = g(x)
    x0: valor inicial
    tol: tolerancia
    max_iter: número máximo de iteraciones
    """
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    raise ValueError("No convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: f(x) = x^3 - x - 2 -> g(x) = (x + 2)^(1/3)
    g = lambda x: (x + 2)**(1/3)
    x0 = 1.0
    raiz, iteraciones = punto_fijo(g, x0)
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones: {iteraciones}")
