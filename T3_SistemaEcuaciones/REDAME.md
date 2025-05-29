Métodos Directos
Estos métodos obtienen la solución exacta del sistema (dentro de los límites de precisión numérica) en un número finito de pasos.

Eliminación Gaussiana

Descripción: Este método transforma el sistema de ecuaciones en una forma triangular superior mediante operaciones elementales y luego resuelve por sustitución hacia atrás.
Fórmula:
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>b</mi><mi>i</mi></msub><mo>−</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><msub><mi>x</mi><mi>j</mi></msub></mrow><msub><mi>a</mi><mrow><mi>i</mi><mi>i</mi></mrow></msub></mfrac><mo separator="true">,</mo><mspace width="1em"></mspace><mi>i</mi><mo>=</mo><mi>n</mi><mo separator="true">,</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo separator="true">,</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo separator="true">,</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">x_i = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j}{a_{ii}}, \quad i = n, n-1, ..., 1</annotation></semantics></math>



Gauss-Jordan

Descripción: Similar a la eliminación gaussiana, pero continúa hasta obtener la matriz identidad, resolviendo directamente para todas las variables.
Fórmula:
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>b</mi><mi>i</mi></msub><mo>−</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn><mo separator="true">,</mo><mi>j</mi><mo mathvariant="normal">≠</mo><mi>i</mi></mrow><mi>n</mi></munderover><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><msub><mi>x</mi><mi>j</mi></msub></mrow><msub><mi>a</mi><mrow><mi>i</mi><mi>i</mi></mrow></msub></mfrac></mrow><annotation encoding="application/x-tex">x_i = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j}{a_{ii}}</annotation></semantics></math>




Métodos Iterativos
Estos métodos aproximan la solución empezando con un valor inicial y mejorándolo iterativamente hasta converger.

Gauss-Seidel

Descripción: Usa los valores más recientes de las variables calculadas en cada iteración para mejorar la convergencia.
Fórmula:
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msubsup><mi>x</mi><mi>i</mi><mrow><mo stretchy="false">(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></msubsup><mo>=</mo><mfrac><mrow><msub><mi>b</mi><mi>i</mi></msub><mo>−</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><msubsup><mi>x</mi><mi>j</mi><mrow><mo stretchy="false">(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></msubsup><mo>−</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mi>i</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><msubsup><mi>x</mi><mi>j</mi><mrow><mo stretchy="false">(</mo><mi>k</mi><mo stretchy="false">)</mo></mrow></msubsup></mrow><msub><mi>a</mi><mrow><mi>i</mi><mi>i</mi></mrow></msub></mfrac></mrow><annotation encoding="application/x-tex">x_i^{(k+1)} = \frac{b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)}}{a_{ii}}</annotation></semantics></math>



Jacobi

Descripción: Cada variable se actualiza usando los valores de la iteración anterior, sin usar los valores nuevos hasta la siguiente iteración.
Fórmula:
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msubsup><mi>x</mi><mi>i</mi><mrow><mo stretchy="false">(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></msubsup><mo>=</mo><mfrac><mrow><msub><mi>b</mi><mi>i</mi></msub><mo>−</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn><mo separator="true">,</mo><mi>j</mi><mo mathvariant="normal">≠</mo><mi>i</mi></mrow><mi>n</mi></munderover><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><msubsup><mi>x</mi><mi>j</mi><mrow><mo stretchy="false">(</mo><mi>k</mi><mo stretchy="false">)</mo></mrow></msubsup></mrow><msub><mi>a</mi><mrow><mi>i</mi><mi>i</mi></mrow></msub></mfrac></mrow><annotation encoding="application/x-tex">x_i^{(k+1)} = \frac{b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j^{(k)}}{a_{ii}}</annotation></semantics></math>

