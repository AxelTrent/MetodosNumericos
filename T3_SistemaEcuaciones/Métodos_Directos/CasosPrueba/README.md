## |Eliminacion Gaussiana Sistema de ecuaciones

Consideremos el siguiente sistema de 3 ecuaciones lineales con 3 incógnitas:

2x₁ + x₂ - x₃ = 8 -x₁ + 3x₂ + 2x₃ = -7 3x₁ - x₂ + 2x₃ = 5


---

## Entrada para el programa

- Ingresa `n = 3` (número de ecuaciones).
- Para la matriz aumentada \[coeficientes | términos independientes\]:

Ecuación 1:   2,  1, -1  |   8
Ecuación 2:  -1,  3,  2  |  -7
Ecuación 3:   3, -1,  2  |   5


---

## Matriz aumentada ingresada

|   2.000    1.000   -1.000  |   8.000 |
|  -1.000    3.000    2.000  |  -7.000 |
|   3.000   -1.000    2.000  |   5.000 |


---

## Ejecución

El algoritmo realiza **eliminación gaussiana**, transformando la matriz en una forma triangular superior.  
Luego, usa **sustitución hacia atrás** para calcular los valores de `x₁`, `x₂` y `x₃`.

---

## Solución final

x[0] = 2.000
x[1] = 1.000
x[2] = -1.000


Esto corresponde a:

x₁ = 2
x₂ = 1
x₃ = -1

---

## Por qué funciona

- La matriz de coeficientes es **no singular** (determinante ≠ 0), lo que garantiza una solución única.
- No hay **división por cero** durante la eliminación gaussiana, ya que los elementos pivote `matriz[j][j]` son distintos de cero.
- El sistema es **linealmente independiente** y **bien condicionado**.

------------------------------------------------------------------------------------------------------------------------------------------


## Error Eliminación Gaussiana Sistema de ecuaciones
Consideremos el siguiente sistema de 2 ecuaciones con 2 incógnitas, donde la matriz es singular (no tiene solución única):
x₁ + x₂ = 2
2x₁ + 2x₂ = 4


## Entrada para el programa
1. Ingresa n = 2
2. Para la matriz aumentada:
   - Ecuación 1: 1, 1 | 2
   - Ecuación 2: 2, 2 | 4

Matriz aumentada ingresada:
| 1.000 1.000 | 2.000|
| 2.000 2.000 | 4.000|


## Ejecución del algoritmo
1. **Eliminación gaussiana**:
   - Se intenta eliminar el elemento matriz[1][0] usando factor = matriz[1][0]/matriz[0][0] = 2/1 = 2
   - Tras la eliminación, la segunda fila queda en ceros:
     ```
     |   1.000    1.000 |    2.000|
     |   0.000    0.000 |    0.000|
     ```

2. **Sustitución hacia atrás**:
   - El algoritmo intenta calcular x[1] como soluciones[1]/matriz[1][1] = 0/0
   - Esto genera una división por cero

## Análisis del fallo
- **Matriz singular**: La matriz de coeficientes tiene determinante = 0
- **Dependencia lineal**: La segunda ecuación es un múltiplo de la primera (2x la primera ecuación)
- **Consecuencia**:
  - matriz[1][1] = 0 en la forma triangular
  - Causa división por cero en la sustitución hacia atrás
- **Naturaleza del sistema**:
  - Tiene infinitas soluciones (o ninguna si los términos independientes no fueran consistentes)
  - El código no está diseñado para manejar estos casos y lanza un error
