## Tema 2: Solución de Ecuaciones

Este tema aborda técnicas numéricas para encontrar las raíces o soluciones de ecuaciones, especialmente aquellas que no se pueden resolver de manera analítica. Estas métodos son esenciales en matemáticas aplicadas, ingeniería y ciencias, donde se necesitan aproximaciones precisas para resolver problemas como determinar puntos de equilibrio, optimizar funciones o modelar sistemas físicos. Los métodos se dividen en dos categorías principales: métodos abiertos y métodos cerrados, cada uno con enfoques distintos para alcanzar soluciones.

### 📂 Métodos Abiertos

Los métodos abiertos parten de un valor inicial y usan iteraciones para converger hacia la raíz, sin requerir que el intervalo contenga la solución de forma garantizada. Son útiles para ecuaciones no lineales y pueden ser más rápidos, pero dependen de una buena elección inicial.

- **Método de Newton-Raphson**  
  Este método utiliza la derivada de la función para acercarse rápidamente a la raíz, siendo ideal para funciones suaves y cuando se tiene una estimación inicial cercana a la solución.

- **Método de Punto Fijo**  
  Este enfoque transforma la ecuación en una forma iterable, buscando un punto donde la función se iguale a su entrada, útil en problemas donde se puede redefinir la ecuación adecuadamente.

  [Ver Carpeta](/T2_SolucionEcuaciones/Métodos Abiertos/)

### 📂 Métodos Cerrados

Los métodos cerrados operan dentro de un intervalo conocido que contiene al menos una raíz, asegurando convergencia bajo ciertas condiciones. Son más robustos y se prefieren cuando no se tiene una buena estimación inicial.

- **Método de Bisección**  
  Este método divide repetidamente un intervalo por la mitad, seleccionando la subsección que contiene la raíz, siendo muy confiable pero lento.

- **Método de Regla Falsa**  
  Similar a la bisección, este método usa una línea recta para aproximar la raíz dentro del intervalo, ofreciendo una convergencia más rápida en algunos casos.

  [Ver Carpeta](/T2_SolucionEcuaciones/Métodos Cerrados/)

### Contenido
- Archivos de código en Python y Excel (.xlsx): `Método_de_Newton-Raphson.py`, `Método_de_Punto_Fijo.xlsx`, `Método_de_Bisección.xlsx`, y `Método_de_Regla_Falsa.xlsx`.

### Recomendación
Revisa el archivo `README.md` dentro de cada carpeta para más detalles sobre la implementación y uso de cada método.
