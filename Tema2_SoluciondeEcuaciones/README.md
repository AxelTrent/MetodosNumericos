📁 Metodos_Cerrados/: Agrupa métodos que necesitan un intervalo donde la función cambie de signo ($f(a) \cdot f(b) < 0$).

Bisección

Regla Falsa

📁 Metodos_Abiertos/: Incluye métodos que no requieren un intervalo inicial, sino uno o dos valores como punto de partida.

Punto Fijo

Newton-Raphson

Secante

Comparación General
Característica	Métodos Cerrados	Métodos Abiertos
Uso de intervalo	Sí, con cambio de signo en los extremos	No, solo se necesita uno o dos valores iniciales
Tipo de convergencia	Lenta pero segura	Más rápida, aunque no siempre garantizada
Dificultad de implementación	Relativamente simple	Puede requerir derivadas o análisis adicional
Ejemplos comunes	Bisección, Regla Falsa	Punto Fijo, Newton-Raphson, Secante

Propósito del Tema
El objetivo principal es que el estudiante:

Distinga entre métodos cerrados y abiertos.

Selecciona y aplica el método adecuado según las características del problema.

Analizar las fortalezas y debilidades de cada enfoque.

Estudiar como cada técnica afecta la velocidad de convergencia y la eficiencia computacional.

Consejos Prácticos
Es recomendable graficar la función antes de elegir un método.

Asegúrate de que se cumplen las condiciones necesarias para aplicar cada método.

Compara el número de iteraciones que requiere cada uno para evaluar su rendimiento.

Notación Usada
$x_r$: Valor aproximado de la raíz.

$f(x)$: Función que se analiza.

$x_n$: Valor en la iteración actual.

$x_{n+1}$: Valor calculado para la siguiente iteración.


