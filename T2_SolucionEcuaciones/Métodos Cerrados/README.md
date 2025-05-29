Los métodos cerrados operan dentro de un intervalo conocido que contiene al menos una raíz, asegurando convergencia bajo ciertas condiciones. Son más robustos y se prefieren cuando no se tiene una buena estimación inicial.

---

#### ➗ Método de Bisección

Este método divide repetidamente un intervalo por la mitad, seleccionando la subsección que contiene la raíz, siendo muy confiable pero lento.

**Fórmula:**

$$
x_{n+1} = \frac{a_n + b_n}{2}
$$

Donde \( a_n \) y \( b_n \) son los extremos del intervalo actual, y se elige el nuevo intervalo según el signo de \( f(x) \).


---
[Ver codigo de Newton-Raphson](/T2_SolucionEcuaciones/Métodos Cerrados/Metodo_Biseccion.py)
#### ➗ Método de Regla Falsa

Similar a la bisección, este método usa una línea recta para aproximar la raíz dentro del intervalo, ofreciendo una convergencia más rápida en algunos casos.

**Fórmula:**

$$
x_{n+1} = a_n - \frac{f(a_n) (b_n - a_n)}{f(b_n) - f(a_n)}
$$

Donde \( a_n \) y \( b_n \) son los extremos del intervalo, y el nuevo punto se calcula con la intersección de la secante.

[Ver codigo de Regla falsa](/T2_SolucionEcuaciones/Métodos Cerrados/Metodo_Flasa.py)

---


