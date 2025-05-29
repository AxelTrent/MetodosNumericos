
---

## Métodos Directos

Estos métodos encuentran la solución exacta (dentro de la precisión numérica) en un número finito de pasos. Se basan en transformar el sistema de ecuaciones para resolverlo directamente.

### Eliminación Gaussiana

**Descripción:**
Convierte el sistema de ecuaciones en una matriz triangular superior usando operaciones elementales (como intercambiar filas, multiplicar por un escalar o sumar múltiplos de filas). Luego, se resuelve el sistema por sustitución hacia atrás, empezando desde la última ecuación hacia la primera.

**Fórmula:**

$$
x_i = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j}{a_{ii}}, \quad i = n, n-1, \ldots, 1  
$$

[Ver código de Eliminación Gaussiana](/Métodos_Directos/Eliminacion_Gaussiana.py)

---

### Gauss-Jordan

**Descripción:**
Es una extensión del método de Gauss. No se detiene al obtener la forma triangular superior, sino que sigue transformando hasta que se obtiene la matriz identidad, lo que permite leer directamente las soluciones sin sustitución.

**Fórmula:**

$$
x_i = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j}{a_{ii}}  
$$

[Ver código de Gauss-Jordan](Métodos_Directos/GaussJordan.py)


---



