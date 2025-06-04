# Casos de Prueba para Método de Gauss-Seidel

## Caso Exitoso: Sistema Diagonalmente Dominante

### Sistema de ecuaciones
4x1 + x2 - x3 = 8
x1 + 5x2 + 2x3 = -7
-x1 + x2 + 6x3 = 5


### Entrada del programa
- Número de ecuaciones (n): 3
- Matriz aumentada:
[4.0, 1.0, -1.0, 8.0]
[1.0, 5.0, 2.0, -7.0]
[-1.0, 1.0, 6.0, 5.0]

- Tolerancia: 0.000001
- Máximo iteraciones: 100

### Proceso de ejecución
1. **Verificación dominancia diagonal**:
 - Cada elemento diagonal es mayor que la suma de los otros elementos en su fila
 - Fila 1: 4 > 1 + 1 = 2
 - Fila 2: 5 > 1 + 2 = 3
 - Fila 3: 6 > 1 + 1 = 2

2. **Iteraciones**:
 - Fórmula de actualización:
   ```
   x[i] = (termino_independiente - suma(coeficientes[j]*x[j])) / diagonal[i]
   ```
 - Converge rápidamente

### Resultado obtenido
x1 = 2.000
x2 = -1.000
x3 = 1.000


### Razones del éxito
- Matriz diagonalmente dominante
- Pivotes no nulos
- Tolerancia adecuada
- Suficientes iteraciones
- Sistema con solución única

---

## Caso Fallido: Sistema No Dominante

### Sistema de ecuaciones
x1 + 4x2 = 1
3x1 + x2 = 2


### Entrada del programa
- Número de ecuaciones (n): 2
- Matriz aumentada:
[1.0, 4.0, 1.0]
[3.0, 1.0, 2.0]

- Tolerancia: 0.000001
- Máximo iteraciones: 100

### Proceso de ejecución
1. **Verificación dominancia diagonal**:
 - Fila 1: 1 < 4 (no dominante)
 - Fila 2: 1 < 3 (no dominante)

2. **Comportamiento iterativo**:
 - Iteración 1: [1.0, -1.0]
 - Iteración 2: [5.0, -13.0] 
 - Iteración 3: [53.0, -157.0]
 - Valores divergen

### Resultado final
No se alcanzó convergencia en 100 iteraciones


### Razones del fallo
- Matriz no diagonalmente dominante
- Valores divergen en iteraciones
- Coeficientes no diagonales muy grandes
- Aunque tiene solución única, el método no converge

### Recomendaciones
- Reordenar ecuaciones
- Aplicar pivoteo
- Considerar otros métodos iterativos
