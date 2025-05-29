## Métodos Directos
Estos métodos encuentran la solución exacta (dentro de la precisión numérica) en un número finito de pasos. Se basan en transformar el sistema de ecuaciones para resolverlo directamente.

### Eliminación Gaussiana
**Descripción:**  
Convierte el sistema de ecuaciones en una matriz triangular superior usando operaciones elementales (como intercambiar filas, multiplicar por un escalar o sumar múltiplos de filas). Luego, se resuelve el sistema por sustitución hacia atrás, empezando desde la última ecuación hacia la primera.

**Fórmula:**  
$$
x_i = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j}{a_{ii}}, \quad i = n, n-1, \ldots, 1
$$


### Gauss-Jordan
**Descripción:**  
Es una extensión del método de Gauss. No se detiene al obtener la forma triangular superior, sino que sigue transformando hasta que se obtiene la matriz identidad, lo que permite leer directamente las soluciones sin sustitución.

**Fórmula:**  
$$
x_i = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j}{a_{ii}}
$$


## Métodos Iterativos
Estos métodos aproximan la solución comenzando con un valor inicial y mejorándolo en cada iteración. Se repiten hasta que la diferencia entre iteraciones es lo suficientemente pequeña.

### Gauss-Seidel
**Descripción:**  
Usa los valores más recientes calculados dentro de la misma iteración. Esto hace que, en muchos casos, converja más rápido que Jacobi.

**Fórmula:**  
$$
x_i^{(k+1)} = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)}}{a_{ii}}
$$


### Jacobi
**Descripción:**  
Cada variable se actualiza usando únicamente los valores de la iteración anterior. No se usan los nuevos valores hasta que termine la iteración, lo que hace que sea más fácil de implementar, pero puede requerir más iteraciones para converger.

**Fórmula:**  
$$
x_i^{(k+1)} = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j^{(k)}}{a_{ii}}
$$


### Método de la Secante
**Descripción:**  
Aproxima la derivada con dos puntos:

**Fórmula:**  
$$
x_{n+1} = x_n - \frac{f(x_n) \cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$


**Ventajas:**  
- No necesita derivadas.  
- Mejora la convergencia frente al punto fijo.

**Desventajas:**  
- Requiere dos valores iniciales.  
- Puede fallar si \( f(x_n) = f(x_{n-1}) \).
