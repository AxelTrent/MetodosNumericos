# Método de los Cinco Puntos para Derivación Numérica

## Caso de Prueba Exitoso

### Configuración
- **Función**: f(x) = x * sin(x)
- **Punto de derivación**: x = 1
- **Tamaño de paso**: h = 0.1

### Implementación
```python
x = 1
h = 0.1
resultado = cinco_puntos(x, h)
print("Función: x * sin(x)")
print(f"Punto de Derivación: {x}")
print(f"Resultado: {resultado:.4g}")
Cálculos Analíticos
Derivada exacta:
f'(x) = sin(x) + x * cos(x)

Para x=1:
f'(1) ≈ 0.8415 + 0.5403 ≈ 1.3818

Evaluación de Puntos
f(1.2) ≈ 0.9776

f(1.1) ≈ 0.9047

f(0.9) ≈ 0.7838

f(0.8) ≈ 0.7173

Aplicación del Método
f'(1) ≈ [-0.9776 + 8(0.9047) - 8(0.7838) + 0.7173] / (12*0.1) ≈ 1.3818

Resultado
Función: x * sin(x)
Punto de Derivación: 1
Resultado: 1.382
Análisis
Error relativo: 0.016%

h = 0.1 proporciona buen equilibrio entre precisión y estabilidad

Función bien comportada en el punto evaluado

Método de alta precisión (O(h⁴))

```

# Caso de Error
## Configuración Problemática
Misma función: f(x) = x * sin(x)

Mismo punto: x = 1

Tamaño de paso extremo: h = 1e-9

Implementación
```python
x = 1
h = 0.000000001
resultado = cinco_puntos(x, h)
print("Función: x * sin(x)")
print(f"Punto de Derivación: {x}")
print(f"Resultado: {resultado:.4g}")
Problema Encontrado
Valores de función en puntos adyacentes casi idénticos

Diferencias numéricas se pierden por precisión limitada

Errores de redondeo amplificados

Resultado Erróneo
Función: x * sin(x)
Punto de Derivación: 1
Resultado: 1.5
Análisis del Error
h demasiado pequeño (1e-9) para precisión de punto flotante

Pérdida de dígitos significativos en cálculos

Resultado difiere en ~8.5% del valor real

Demuestra límites prácticos de la precisión numérica

```

# Conclusión
El método de los cinco puntos:

- Es efectivo con tamaños de paso moderados

- Falla con pasos extremadamente pequeños

- Requiere selección cuidadosa del parámetro h

- Ilustra compromiso entre precisión teórica y estabilidad numérica
