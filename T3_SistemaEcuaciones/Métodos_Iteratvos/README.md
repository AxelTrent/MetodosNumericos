## Métodos Iterativos

Estos métodos aproximan la solución comenzando con un valor inicial y mejorándolo en cada iteración. Se repiten hasta que la diferencia entre iteraciones es lo suficientemente pequeña.

### Gauss-Seidel

**Descripción:**
Usa los valores más recientes calculados dentro de la misma iteración. Esto hace que, en muchos casos, converja más rápido que Jacobi.

**Fórmula:**

$$
x_i^{(k+1)} = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)}}{a_{ii}}  
$$

[Ver código de Gauss_Seidel](Métodos_Iterativos/Gauss_Seidel.py)

---

### Jacobi

**Descripción:**
Cada variable se actualiza usando únicamente los valores de la iteración anterior. No se usan los nuevos valores hasta que termine la iteración, lo que hace que sea más fácil de implementar, pero puede requerir más iteraciones para converger.

**Fórmula:**

$$
x_i^{(k+1)} = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j^{(k)}}{a_{ii}}  
$$

[Ver código de Jacobi](Métodos_Iterativos/Jacobi.py)

---

### Método de la Secante

**Descripción:**
Aproxima la derivada con dos puntos:

**Fórmula:**

$$
x_{n+1} = x_n - \frac{f(x_n) \cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}  
$$

[Ver código de Secante](Métodos_Iterativos/Secante.py)

**Ventajas:**

* No necesita derivadas.
* Mejora la convergencia frente al punto fijo.

**Desventajas:**

* Requiere dos valores iniciales.
* Puede fallar si

$$
f(x_n) = f(x_{n-1})  
$$

---

