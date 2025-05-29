Estos métodos estiman valores intermedios de una función a partir de puntos conocidos, útiles para completar datos o crear curvas.

---

#### 📏 Interpolación Lineal

Conecta dos puntos con una recta para estimar valores intermedios, usado en análisis de datos temporales.

**Fórmula:**

$$
f(x) = f(x_0) + \frac{f(x_1) - f(x_0)}{x_1 - x_0} (x - x_0)
$$

---

#### 📐 Interpolación Polinómica

Usa un polinomio para interpolar varios puntos, aplicado en diseño de curvas o análisis de señales.

**Fórmula (Lagrange para tres puntos):**

$$
P(x) = \sum_{i=0}^n f(x_i) \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}
$$

---

### 📄 Contenido

Archivos de código en Python:  
`Correlacion.py`, `MinimosCuadrados.py`, `RegresionLineal.py`, `InterpolacionLineal.py`, `InterpolacionPolinomica.py`

---
