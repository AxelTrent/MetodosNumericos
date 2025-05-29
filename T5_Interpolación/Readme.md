## Tema 5: Interpolación y Análisis de Datos

En este tema se exploran técnicas numéricas relacionadas con la interpolación y el análisis de datos, herramientas clave en el análisis matemático, científico y computacional. La interpolación ayuda a estimar valores intermedios a partir de datos conocidos, mientras que el análisis de datos se enfoca en identificar patrones o relaciones entre variables. Estas técnicas son esenciales en diversas áreas, como la ingeniería, las ciencias naturales, la economía y la tecnología, donde se requiere interpretar o predecir información a partir de datos discretos o experimentales.

### 📂 Método de Análisis de Datos

Los métodos de análisis de datos permiten modelar y entender las relaciones entre diferentes variables a partir de un conjunto de información recopilada. Son útiles para descubrir tendencias, hacer predicciones o evaluar la calidad de los datos en estudios prácticos.

- **Correlación**  
  Este método se utiliza para medir cuán relacionadas están dos variables, indicando si un cambio en una tiende a acompañarse de un cambio en la otra. Es muy común en campos como la estadística y las ciencias sociales para analizar si existe una conexión, por ejemplo, entre el tiempo de estudio y las calificaciones de los estudiantes, o entre la temperatura y el consumo de energía.

- **Mínimos Cuadrados**  
  Esta técnica se emplea para ajustar una curva, generalmente una recta o un polinomio, a un conjunto de datos, buscando la mejor representación posible de la relación entre las variables. Se usa ampliamente en áreas como la economía para predecir tendencias de mercado, en la física para ajustar modelos experimentales, o en la biología para analizar el crecimiento de poblaciones.

- **Regresión Lineal**  
  La regresión lineal es un enfoque específico que busca encontrar una recta que represente la relación entre dos variables, una dependiente y otra independiente. Es ideal para hacer predicciones simples, como estimar ventas basadas en publicidad o analizar cómo afecta la altura al peso corporal, y es una herramienta básica en el aprendizaje automático y el análisis de datos.

  [Ver Carpeta](/T5_Interpolación/Método_Analisis_Datos/)

### 📂 Métodos de Interpolación

Los métodos de interpolación permiten estimar valores de una función en puntos intermedios cuando solo se tienen datos en algunos lugares específicos. Son útiles para llenar huecos en la información, crear gráficos suaves o simular comportamientos continuos a partir de mediciones discretas.

- **Interpolación Lineal**  
  Este es el método más básico de interpolación, que conecta dos puntos consecutivos con una línea recta para estimar valores intermedios. Es fácil de aplicar y se usa en situaciones como el diseño de animaciones o el análisis de datos temporales, como temperaturas diarias, aunque funciona mejor cuando los cambios entre puntos son pequeños.

- **Interpolación Polinómica**  
  Este método construye una curva suave que pasa por todos los puntos dados, utilizando un polinomio que puede adaptarse a más de dos puntos. Es más sofisticado y se emplea en ingeniería para diseñar trayectorias o en el análisis de señales, aunque puede volverse menos preciso si hay muchos puntos o los datos son irregulares.

  [Ver Carpeta](/T5_Interpolación/Métodos_Interpolación/)

### Contenido
- Archivos de código en Python que implementan cada técnica: `Correlacion.py`, `MinimosCuadrados.py`, `RegresionLineal.py`, `InterpolacionLineal.py` y `InterpolacionPolinomica.py`.

### Recomendación
Revisa el archivo `README.md` dentro de cada carpeta para más detalles sobre la implementación y uso de cada método.
