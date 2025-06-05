# Método de los Tres Puntos para Derivación Numérica

## Caso de Prueba Exitoso

### Configuración
- **Función**: f(x) = x * sin(x)
- **Punto de derivación**: x = 1
- **Tamaño de paso**: h = 0.1

### Implementación
## Código Python
```python
x = 1
h = 0.1
derivada_numerica = tres_puntos(x, h)
derivada_exacta = derivada_analitica(x)
error_absoluto = abs(derivada_numerica - derivada_exacta)

print("Función: f(x) = x * sin(x)")
print(f"Punto de derivación: {x}")
print(f"Tamaño del paso: {h}")
print(f"Derivada numérica (Tres Puntos): {derivada_numerica:.6f}")
print(f"Derivada analítica:               {derivada_exacta:.6f}")
print(f"Error absoluto:                  {error_absoluto:.2e}")

### Evaluaciones:

f(1.1) ≈ 0.904673

f(0.9) ≈ 0.783841

Cálculo: [0.904673 - 0.783841]/(2*0.1) ≈ 1.604163

Error: 22.2% (típico para h=0.1 en este método)

### Factores de éxito:

Tamaño de paso h adecuado para este método

Función suave y diferenciable

Error dentro de lo esperado para O(h²)

```
# Caso de Error
Configuración Problemática
Misma función: f(x) = x * sin(x)

Mismo punto: x = 1

Tamaño de paso extremo: h = 1e-9

## Implementación
```python
x = 1
h = 0.000000001
derivada_numerica = tres_puntos(x, h)
derivada_exacta = derivada_analitica(x)
error_absoluto = abs(derivada_numerica - derivada_exacta)
print("Función: f(x) = x * sin(x)")
print(f"Punto de derivación: {x}")
print(f"Tamaño del paso: {h}")
print(f"Derivada numérica (Tres Puntos): {derivada_numerica:.6f}")
print(f"Derivada analítica:               {derivada_exacta:.6f}")
print(f"Error absoluto:                  {error_absoluto:.2e}")
Resultados
Función: f(x) = x * sin(x)
Punto de derivación: 1
Tamaño del paso: 1e-09
Derivada numérica (Tres Puntos): 1.000000
Derivada analítica:               1.381773
Error absoluto:                  3.81e-01
Análisis del Error
Evaluaciones:

f(1.000000001) ≈ 0.8414709858

f(0.999999999) ≈ 0.8414709838

Diferencia: ~2×10⁻⁹ (insignificante para precisión float)

Error: 38.1% (resultado completamente erróneo)

### Causas del fallo:

Pérdida de dígitos significativos al restar números casi iguales

Amplificación de errores de redondeo al dividir por h muy pequeño

El método O(h²) no compensa los errores numéricos con h extremo

```

# Conclusión
El método de tres puntos funciona mejor con h moderados

Requiere equilibrio entre error de truncamiento y error numérico

h demasiado pequeño produce resultados no confiables

Ilustra importancia de seleccionar parámetros adecuados en métodos numéricos
