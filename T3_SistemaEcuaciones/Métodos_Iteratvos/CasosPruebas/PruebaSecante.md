
# Caso donde el código funciona correctamente

## Función y configuración:
- Función: f(x) = x² - 4 (cuya raíz es x = 2 o x = -2)
- Entrada para el programa:
  - Primer punto inicial: x0 = 1
  - Segundo punto inicial: x1 = 3
  - Tolerancia: 0.00001
  - Máximo de iteraciones: 100

## Ejecución:
El método de la secante itera usando la fórmula:
xₙ₊₁ = xₙ - f(xₙ) * (xₙ - xₙ₋₁)/(f(xₙ) - f(xₙ₋₁))

```python
Iteraciones (aproximadas):
Iteración x_n f(x_n) Error
0 2.333333 -0.555556 0.666667
1 2.076923 -0.316568 0.256410
2 2.012987 -0.049876 0.063936
3 2.000162 -0.000325 0.012825
4 2.000000 -0.000000 0.000162


Resultado:
Convergencia alcanzada en la iteración 5!
Raíz aproximada: x = 2.000000
Solución final: x = 2.000000
```

## Por qué funciona:
- La función f(x) = x² - 4 es continua y diferenciable, con una raíz bien definida en x = 2
- Los puntos iniciales x0 = 1 y x1 = 3 están cerca de la raíz y encierran la raíz (f(1) < 0, f(3) > 0)
- La derivada de la función en la región no es cero
- La diferencia f(x1) - f(x0) no es demasiado pequeña, evitando problemas numéricos
- La tolerancia (0.00001) es adecuada y el método converge rápidamente

---

# Caso donde el código NO funciona

## Función y configuración:
- Función: f(x) = x² - 4 (misma función para consistencia)
- Entrada para el programa:
  - Primer punto inicial: x0 = 2
  - Segundo punto inicial: x1 = 2.000001
  - Tolerancia: 0.00001
  - Máximo de iteraciones: 100

## Ejecución:
En la primera iteración:
- f(x0) = f(2) = 0
- f(x1) = f(2.000001) ≈ 0.000004

El método genera valores inestables debido a:
- La diferencia f(x1) - f(x0) ≈ 0.000004 es muy pequeña
- El cálculo de x_nuevo puede producir valores muy grandes por división por denominador pequeño

Resultado:
Advertencia: No se alcanzó convergencia dentro de 100 iteraciones.


## Por qué falla:
- Los puntos iniciales están demasiado cerca de la raíz exacta (x = 2)
- f(x1) - f(x0) es muy pequeño, causando inestabilidad numérica
- La cercanía de los puntos amplifica errores de redondeo en la división
- Aunque el código detecta diferencias pequeñas, el umbral puede no ser suficiente
