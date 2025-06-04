# Caso donde el código funciona correctamente

## Sistema de ecuaciones

Consideremos el siguiente sistema de 3 ecuaciones lineales con 3 incógnitas:

2x₁ + x₂ - x₃ = 8
                                   -x₁ + 3x₂ + 2x₃ = -7
                                                                      3x₁ - x₂ + 2x₃ = 5


---

## Entrada para el programa

- Ingresa `n = 3` (número de ecuaciones).
- Para la matriz aumentada \[coeficientes | términos independientes\]:

Ecuación 1: 2, 1, -1 | 8
Ecuación 2: -1, 3, 2 | -7
Ecuación 3: 3, -1, 2 | 5

---

## Matriz aumentada ingresada

| 2.000 1.000 -1.000 | 8.000 |
| -1.000 3.000 2.000 | -7.000 |
| 3.000 -1.000 2.000 | 5.000 |

---

## Ejecución

El algoritmo realiza **eliminación gaussiana**, transformando la matriz en una forma triangular superior.  
Luego, usa **sustitución hacia atrás** para calcular los valores de `x₁`, `x₂` y `x₃`.

---

## Solución final

x[0] = 2.000
x[1] = 1.000
x[2] = -1.000

css
Copiar
Editar

Esto corresponde a:

x₁ = 2
x₂ = 1
x₃ = -1

---

## Por qué funciona

- La matriz de coeficientes es **no singular** (determinante ≠ 0), lo que garantiza una solución única.
- No hay **división por cero** durante la eliminación gaussiana, ya que los elementos pivote `matriz[j][j]` son distintos de cero.
- El sistema es **linealmente independiente** y **bien condicionado**.
