Los métodos abiertos parten de un valor inicial y usan iteraciones para converger hacia la raíz, sin requerir que el intervalo contenga la solución de forma garantizada. Son útiles para ecuaciones no lineales y pueden ser más rápidos, pero dependen de una buena elección inicial.

- **Método de Newton-Raphson**  
  Este método utiliza la derivada de la función para acercarse rápidamente a la raíz, siendo ideal para funciones suaves y cuando se tiene una estimación inicial cercana a la solución.  
  **Fórmula:**  
  $$
  x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
  $$  
  Donde `x_n` es la aproximación actual, `f(x_n)` es el valor de la función, y `f'(x_n)` es su derivada.

- **Método de Punto Fijo**  
  Este enfoque transforma la ecuación en una forma iterable, buscando un punto donde la función se iguale a su entrada, útil en problemas donde se puede redefinir la ecuación adecuadamente.  
  **Fórmula:**  
  $$
  x_{n+1} = g(x_n)
  $$  
  Donde `g(x)` es una función reformulada a partir de la ecuación original `f(x) = 0`, como `g(x) = x - f(x)`.
