Estos métodos estudian relaciones entre variables para entender datos y hacer predicciones.

---

#### 📊 Correlación

Mide si dos variables están relacionadas, útil en estadística para analizar conexiones, como entre clima y consumo energético.

**Fórmula (coeficiente de correlación de Pearson):**

$$
r = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sqrt{\sum{(x_i - \bar{x})^2} \sum{(y_i - \bar{y})^2}}}
$$

---

[Ver codigo de Correlacionr](/T5_Interpolación/Método_Analisis_Datos/Correlacion.py)

#### 📈 Mínimos Cuadrados

Ajusta una curva a los datos para modelar relaciones, usado en economía o física para predecir tendencias.

**Fórmulas (pendiente y ordenada para regresión lineal):**

$$
m = \frac{n \sum{(x_i y_i)} - \sum{x_i} \sum{y_i}}{n \sum{(x_i^2)} - (\sum{x_i})^2}
$$

$$
b = \frac{\sum{y_i} - m \sum{x_i}}{n}
$$

---
[Ver codigo de Minimos CUadrados](/T5_Interpolación/Método_Analisis_Datos/MinimosCuadrados.py)
#### 📉 Regresión Lineal

Encuentra una recta que represente la relación entre dos variables, común para predicciones como ventas según publicidad.

**Fórmula:**

$$
y = mx + b
$$

[Ver codigo de Regresión Lineal](/T5_Interpolación/Método_Analisis_Datos/RegresionLineal.py)
---
