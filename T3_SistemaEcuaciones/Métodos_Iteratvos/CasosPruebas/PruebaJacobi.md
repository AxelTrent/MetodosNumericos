# Caso donde el código funciona correctamente

## Sistema de ecuaciones:
Consideremos el siguiente sistema de 3 ecuaciones con 3 incógnitas, diseñado para ser diagonalmente dominante, lo que favorece la convergencia del método de Jacobi:
4x₁ + x₂ - x₃ = 8
x₁ + 5x₂ + x₃ = -7
-x₁ + x₂ + 6x₃ = 5

```python
### Entrada para el programa:
- Ingresa n = 3 (número de ecuaciones).
- Para la matriz aumentada [coeficientes | términos independientes]:
  - Ecuación 1: 4, 1, -1 | 8
  - Ecuación 2: 1, 5, 1 | -7
  - Ecuación 3: -1, 1, 6 | 5
- Tolerancia: 0.00001
- Máximo de iteraciones: 100

### Matriz aumentada ingresada:
| 4.000 1.000 -1.000 | 8.000 |
| 1.000 5.000 1.000 | -7.000 |
| -1.000 1.000 6.000 | 5.000 |


### Ejecución:
El método de Jacobi itera, calculando los valores de x[i] usando la fórmula:
x[i] = (soluciones[i] - Σ(matriz[i][j] * anterior[j], j ≠ i)) / matriz[i][i]


- La matriz es diagonalmente dominante (el valor absoluto del elemento diagonal en cada fila es mayor que la suma de los valores absolutos de los demás elementos de la fila), lo que garantiza la convergencia.
- Solución aproximada (tras varias iteraciones, dependiendo de la tolerancia):
x[0] = 2.000
x[1] = -1.000
x[2] = 1.000

Esto corresponde a x₁ = 2, x₂ = -1, x₃ = 1.
```

### Por qué funciona:
- La matriz es diagonalmente dominante, una condición suficiente para la convergencia del método de Jacobi.
- Los elementos diagonales (matriz[i][i]) son no nulos (4, 5, 6), evitando divisiones por cero, y el código incluye una validación para detectar diagonales cercanas a cero.
- La tolerancia (0.00001) es adecuada, y el número máximo de iteraciones (100) es suficiente para alcanzar la convergencia.
- El sistema tiene una solución única, y las iteraciones convergen cuando la diferencia máxima entre iteraciones (|x[i] - anterior[i]|) es menor o igual a la tolerancia.

---

# Caso donde el código NO funciona

## Sistema de ecuaciones:
Consideremos el siguiente sistema de 2 ecuaciones con 2 incógnitas, que no es diagonalmente dominante y no converge con el método de Jacobi:
x₁ + 4x₂ = 1
3x₁ + x₂ = 2


### Entrada para el programa:
- Ingresa n = 2.
- Para la matriz aumentada:
  - Ecuación 1: 1, 4 | 1
  - Ecuación 2: 3, 1 | 2
- Tolerancia: 0.00001
- Máximo de iteraciones: 100

### Matriz aumentada ingresada:
- | 1.000 4.000 | 1.000 |
- | 3.000 1.000 | 2.000 |


### Ejecución:
El método de Jacobi itera, pero los valores de x[i] oscilan o divergen debido a la falta de dominancia diagonal.

Por ejemplo:
- Iteración 1: x[0] = 1.000, x[1] = 2.000
- Iteración 2: x[0] = -7.000, x[1] = -1.000
- Iteración 3: x[0] = 5.000, x[1] = 5.000

Los valores no convergen, y el algoritmo alcanza el máximo de iteraciones (100), mostrando:
Advertencia: No se alcanzó convergencia dentro del número de iteraciones establecidas


### Por qué falla:
- La matriz no es diagonalmente dominante (en la primera fila, |1| < |4|, y en la segunda, |1| < |3|), lo que viola una condición clave para la convergencia del método de Jacobi.
- Las iteraciones producen valores que oscilan o divergen debido al peso significativo de los coeficientes no diagonales.
- Aunque el sistema tiene una solución única (x₁ = 1/11, x₂ = 5/11), el método de Jacobi no converge para esta matriz sin reordenar las ecuaciones o aplicar técnicas adicionales.
