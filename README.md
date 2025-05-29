### Introducción a los métodos numéricos

Los métodos numéricos son técnicas matemáticas y computacionales que permiten resolver problemas complejos aproximando soluciones cuando no es posible obtenerlas de forma analítica. A continuación, se detalla cada punto solicitado:

#### 1.1 **Importancia de los métodos numéricos**
Los métodos numéricos son fundamentales en ciencias e ingeniería porque:
- **Resuelven problemas no analíticos**: Muchos problemas reales (ecuaciones diferenciales, integrales complejas, etc.) no tienen solución exacta o son muy difíciles de resolver analíticamente.
- **Optimización y eficiencia**: Permiten modelar y simular sistemas complejos (clima, estructuras, finanzas, etc.) en computadoras.
- **Aplicaciones prácticas**: Se usan en física, ingeniería, economía, biología, inteligencia artificial, entre otros, para obtener resultados aproximados con alta precisión.
- **Automatización**: Facilitan el uso de software para resolver problemas a gran escala, ahorrando tiempo y recursos.

#### 1.2 **Conceptos básicos**
- **Cifra significativa**: Dígitos en un número que contribuyen a su precisión. Por ejemplo, en 3.140, hay 4 cifras significativas.
- **Precisión**: Nivel de detalle en la representación de un valor numérico, relacionado con la cantidad de cifras significativas.
- **Exactitud**: Cercanía entre el valor calculado y el valor real. Un cálculo puede ser preciso (muchos dígitos) pero no exacto (lejos del valor verdadero).
- **Incertidumbre**: Margen de error o imprecisión en una medición o cálculo, debido a limitaciones en instrumentos o métodos.
- **Sesgo**: Error sistemático que desvía consistentemente los resultados en una dirección, por ejemplo, debido a un modelo matemático incorrecto.

#### 1.3 **Tipos de errores**
- **Error absoluto**: Diferencia entre el valor real y el valor aproximado.  
  **Fórmula:**  
  $$
  |x - \hat{x}|
  $$  
  Donde `x` es el valor real y `\hat{x}` es el valor aproximado.
- **Error relativo**: Error absoluto dividido por el valor real.  
  **Fórmula:**  
  $$
  \frac{|x - \hat{x}|}{|x|}
  $$  
  Donde los términos son los mismos que en el error absoluto.
- **Error de redondeo**: Surge al limitar el número de cifras significativas en cálculos, común en computadoras con precisión finita.
- **Error de truncamiento**: Ocurre al aproximar una función o proceso infinito (como series o integrales) por uno finito.
- **Error inherente**: Proviene de datos iniciales imprecisos o incertidumbre en las mediciones.
- **Error de propagación**: Cuando los errores en las entradas se amplifican en cálculos posteriores.

#### 1.4 **Software de cómputo numérico**
Herramientas comunes para implementar métodos numéricos incluyen:
- **MATLAB**: Ampliamente usado en ingeniería y ciencias por su facilidad para manejar matrices y visualización.
- **Python**: Con bibliotecas como NumPy, SciPy y Matplotlib, es versátil y de código abierto.
- **R**: Ideal para estadística y análisis de datos.
- **Mathematica y Maple**: Para cálculos simbólicos y numéricos avanzados.
- **C++ y Fortran**: Usados en aplicaciones de alto rendimiento donde la velocidad es crítica.
- **Julia**: Lenguaje moderno optimizado para cálculos numéricos y científicos.

#### 1.5 **Métodos iterativos**
Los métodos iterativos generan una secuencia de soluciones aproximadas que convergen hacia la solución exacta. Características:
- **Definición**: Parten de una aproximación inicial y la refinan iterativamente hasta alcanzar un criterio de convergencia (error aceptable).
- **Ejemplos**:
  - **Método de Newton-Raphson**: Para encontrar raíces de ecuaciones no lineales, usando derivadas.  
    **Fórmula:**  
    $$
    x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
    $$  
    Donde `x_n` es la aproximación actual, `f(x_n)` es el valor de la función, y `f'(x_n)` es su derivada.
  - **Método de Gauss-Seidel y Jacobi**: Para resolver sistemas de ecuaciones lineales.
  - **Método del punto fijo**: Transforma una ecuación en una forma \( x = g(x) \) y aproxima iterativamente.  
    **Fórmula:**  
    $$
    x_{n+1} = g(x_n)
    $$  
    Donde `g(x)` es una función reformulada.
  - **Métodos de optimización**: Como el descenso por gradiente, usado en machine learning.
- **Ventajas**: Eficientes para problemas grandes, especialmente en sistemas lineales o no lineales.
- **Desventajas**: Dependen de una buena elección inicial y pueden no converger si el método no es adecuado.

### Recomendación
Revisa los archivos `README.md` de cada sección para más detalles sobre la implementación y uso de estos métodos.
