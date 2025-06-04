# Análisis de casos para resolución de sistemas lineales

## Caso 1: Sistema con solución única (funciona correctamente)

### Sistema de ecuaciones
2x₁ + x₂ - x₃ = 8
-x₁ + 3x₂ + 2x₃ = -7
3x₁ - x₂ + 2x₃ = 5


### Proceso de solución

**Matriz aumentada inicial:**
| 2.000 1.000 -1.000 | 8.000 |
| -1.000 3.000 2.000 | -7.000 |
| 3.000 -1.000 2.000 | 5.000 |


**Pasos del algoritmo:**
1. Normalización de la primera fila (pivote = 2.000)
2. Eliminación de elementos en columna 1 de filas 2 y 3
3. Normalización de la segunda fila (nuevo pivote)
4. Eliminación de elementos en columna 2
5. Normalización de la tercera fila

**Matriz final (forma escalonada reducida):**
| 1.000 0.000 0.000 | 2.000 |
| 0.000 1.000 0.000 | 1.000 |
| 0.000 0.000 1.000 | -1.000 |


**Solución obtenida:**
x₁ = 2.000
x₂ = 1.000
x₃ = -1.000


### Por qué funciona
- Matriz no singular (determinante ≠ 0)
- Todos los pivotes son diferentes de cero
- Sistema linealmente independiente
- Método converge correctamente

---

## Caso 2: Sistema sin solución (falla)

### Sistema de ecuaciones
x₁ + x₂ = 2
x₁ + x₂ = 3


### Proceso de solución

**Matriz aumentada inicial:**
| 1.000 1.000 | 2.000 |
| 1.000 1.000 | 3.000 |


**Pasos del algoritmo:**
1. Primera iteración (i=0):
   - Pivote = 1.000
   - Normalización primera fila
   - Eliminación en fila 2

**Matriz después de eliminación:**
| 1.000 1.000 | 2.000 |
| 0.000 0.000 | 1.000 |


2. Segunda iteración (i=1):
   - Intenta dividir por pivote = 0.000 → **Error de división por cero**

### Por qué falla
- Matriz singular (determinante = 0)
- Ecuaciones linealmente dependientes pero inconsistentes
- Sistema no tiene solución
- Algoritmo no maneja casos con pivote cero

**Interpretación:**
- Fila de ceros con término independiente ≠ 0 → Sistema incompatible
- No existe solución que satisfaga ambas ecuaciones simultáneamente
