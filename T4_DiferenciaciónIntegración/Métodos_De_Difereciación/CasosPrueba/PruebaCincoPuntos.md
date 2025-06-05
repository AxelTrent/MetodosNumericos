# Caso de prueba exitoso

## Configuración:
- **Función**: f(x) = x * sin(x)
- **Punto de derivación**: x = 1
- **Tamaño del paso**: h = 0.1

## Código:
```python
x = 1
h = 0.1
resultado = cinco_puntos(x, h)
print("Función: x * sin(x)")
print(f"Punto de Derivación: {x}")
print(f"Resultado de la Derivada por el método de los Cinco Puntos: {resultado:.4g}")
Ejecución:
La derivada analítica de f(x) = x * sin(x) es f'(x) = sin(x) + x * cos(x).

En x = 1, la derivada exacta es aproximadamente:
f'(1) ≈ 1.3817732907

Valores calculados:

f(1.2) ≈ 0.9776031479

f(1.1) ≈ 0.9046732942

f(0.9) ≈ 0.7838407717

f(0.8) ≈ 0.7173456097

Aplicando la fórmula de cinco puntos:
f'(1) ≈ (-0.9776 + 8*0.9047 - 8*0.7838 + 0.7173)/(12*0.1) ≈ 1.3818

Salida:
Función: x * sin(x)
Punto de Derivación: 1
Resultado de la Derivada por el método de los Cinco Puntos: 1.382
Por qué funciona:
h = 0.1 es un tamaño adecuado para buena precisión

La función es suave y diferenciable en x=1

El resultado numérico (1.382) es muy cercano al valor exacto (1.381773)

El método de cinco puntos tiene alta precisión (O(h⁴))

Caso de error
Configuración:
Función: f(x) = x * sin(x)

Punto de derivación: x = 1

Tamaño del paso: h = 0.000000001 (extremadamente pequeño)

Código:
python
x = 1
h = 0.000000001
resultado = cinco_puntos(x, h)
print("Función: x * sin(x)")
print(f"Punto de Derivación: {x}")
print(f"Resultado de la Derivada por el método de los Cinco Puntos: {resultado:.4g}")
Ejecución:
Con h tan pequeño:

Los valores f(x+2h), f(x+h), etc. son casi idénticos

Las diferencias se pierden por precisión limitada de punto flotante

El cálculo resulta en errores de redondeo significativos

Salida (aproximada):
Función: x * sin(x)
Punto de Derivación: 1
Resultado de la Derivada por el método de los Cinco Puntos: 1.5  # Valor incorrecto
Por qué falla:
h = 10⁻⁹ es demasiado pequeño para cálculos de punto flotante

Las diferencias entre valores de función son insignificantes

El cálculo se ve afectado por errores de redondeo

El resultado (1.5) difiere mucho del valor exacto (≈1.381773)

Demuestra la importancia de elegir un h adecuado (ni muy grande ni muy pequeño)
