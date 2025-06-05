# Cálculo Numérico de Derivadas: Métodos de los Tres y Cinco Puntos

Este proyecto contiene implementaciones en Python de dos métodos numéricos para calcular la derivada de una función en un punto dado: el método de los tres puntos y el método de los cinco puntos. Ambos métodos aproximan la derivada primera de la función $$\( f(x) = x \sin(x) \)$$ utilizando diferencias finitas, pero difieren en precisión y complejidad. A continuación, se presenta una introducción a los métodos y los casos de prueba diseñados para evaluar su comportamiento.

## Introducción a los Métodos y Casos de Prueba

### Método de los Tres Puntos
Aproxima la derivada primera usando la fórmula de diferencia centrada:
$$\[ f'(x) \approx \frac{f(x + h) - f(x - h)}{2h} \]$$

[Ver prueba tres puntos](/T4_DiferenciaciónIntegración/Métodos_De_Difereciación/CasosPrueba/PruebaCincoPuntos.md)

Es simple y tiene un error de truncamiento de orden \( O(h^2) \), pero es menos preciso que el método de los cinco puntos y sensible a valores extremos de \( h \).

### Método de los Cinco Puntos
Utiliza una fórmula más elaborada:
$$\[ f'(x) \approx \frac{-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)}{12h} \]$$

[Ver prueba cinco puntos](/T4_DiferenciaciónIntegración/Métodos_De_Difereciación/CasosPrueba/PruebaTresPuntos.md)

Ofrece mayor precisión con un error de orden \( O(h^4) \). Sin embargo, requiere evaluar la función en más puntos, lo que aumenta el costo computacional.

## Casos de Prueba

Los casos de prueba están diseñados para evaluar el desempeño de cada método:

- **Casos exitosos**: Configuraciones con un tamaño de paso \( h \) adecuado, donde la función es suave y los métodos producen aproximaciones cercanas a la derivada analítica.

- **Casos fallidos**: Configuraciones con valores de \( h \) extremadamente pequeños, donde los errores de redondeo en la aritmética de punto flotante generan resultados inexactos.

Estos casos ilustran las fortalezas y limitaciones de cada método, proporcionando una base para entender su aplicabilidad y la importancia de elegir un tamaño de paso adecuado para minimizar errores numéricos.
