
---

## Integración Numérica

Los métodos de integración numérica permiten calcular la integral definida de una función aproximándola mediante sumas de áreas. Estos métodos son esenciales cuando la función no tiene una antiderivada elemental o cuando se trabaja con datos tabulados. A continuación, se describen los métodos incluidos con mayor detalle:

---

### **Cuadratura Gaussiana**

La cuadratura gaussiana es una técnica avanzada para aproximar integrales definidas, diseñada para ser lo más precisa posible al elegir puntos y pesos óptimos. A diferencia de otros métodos que usan puntos equidistantes, este método selecciona puntos (llamados puntos de Gauss) y sus respectivos pesos para minimizar el error de aproximación. Es particularmente eficiente para integrales en intervalos específicos y para funciones polinómicas, pudiendo integrar exactamente polinomios de grado hasta $2n - 1$ con $n$ puntos. Se usa ampliamente en física y en ingeniería, por ejemplo, en el cálculo de momentos o en simulaciones de dinámica de fluidos.

**Fórmula general:**

$$
\int_a^b f(x)\, dx \approx \sum_{i=1}^n w_i f(x_i)
$$

Donde $w_i$ son los pesos y $x_i$ son los puntos de Gauss, que dependen del intervalo $[a, b]$ y del número de puntos $n$. Para aplicarlo, se transforma el intervalo $[a, b]$ al intervalo estándar $[-1, 1]$, y los valores de $w_i$ y $x_i$ se obtienen de tablas predefinidas o mediante algoritmos específicos.
[Ver código de Cuadratura Gaussiana](/T4_DiferenciaciónIntegración/Métodos_De_Integración/CuadraturaGaussiana.py)
---

### **Simpson 1/3**

El método de Simpson 1/3 aproxima una integral ajustando una parábola a tres puntos consecutivos de la función, lo que lo hace más preciso que el método del trapecio para funciones suaves y bien comportadas. Este método asume que la función puede aproximarse localmente como un polinomio cuadrático, y es muy utilizado en problemas de ingeniería y física, como el cálculo de áreas bajo curvas experimentales o el trabajo realizado por una fuerza variable. Su error de truncamiento es del orden de $h^4$, lo que lo hace bastante preciso para intervalos pequeños.

**Fórmula:**

$$
\int_a^b f(x)\, dx \approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + f(x_2) \right]
$$

Donde $h = \frac{b - a}{2}$, y los puntos son $x_0 = a$, $x_1 = \frac{a + b}{2}$, $x_2 = b$. El coeficiente 4 para el punto central refleja que la parábola da más peso al valor en el medio, mejorando la precisión de la aproximación.

[Ver código de Simpaon 1/3](/T4_DiferenciaciónIntegración/Métodos_De_Integración/Simpson1_3.py)
---

### **Simpson 3/8**

El método de Simpson 3/8 es una variante del método de Simpson que utiliza cuatro puntos, ajustando un polinomio cúbico en lugar de uno cuadrático. Esto lo hace más preciso para funciones más complejas o intervalos más grandes, ya que puede capturar mejor las variaciones de la función. Aunque es un poco más complicado que el método 1/3, sigue siendo fácil de implementar y es útil en aplicaciones como el cálculo de volúmenes o el análisis de datos experimentales. Su error de truncamiento es también del orden de $h^4$, pero puede ser más preciso para ciertos tipos de funciones.

**Fórmula:**

$$
\int_a^b f(x)\, dx \approx \frac{3h}{8} \left[ f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3) \right]
$$

Donde $h = \frac{b - a}{3}$, y los puntos son equidistantes: $x_0 = a$, $x_1 = a + h$, $x_2 = a + 2h$, $x_3 = b$. Los coeficientes 3 para los puntos intermedios reflejan la contribución del polinomio cúbico ajustado.

[Ver código de Simpaon 3/8](/T4_DiferenciaciónIntegración/Métodos_De_Integración/Simpson3_8.py)
---

### **Trapecio**

El método del trapecio es una técnica básica para aproximar integrales, que interpreta el área bajo la curva como una serie de trapecios. Es el método más simple de los presentados, pero también el menos preciso, con un error de truncamiento del orden de $h^2$. A pesar de esto, es muy útil para funciones lineales o casi lineales, y se usa frecuentemente en aplicaciones iniciales o cuando se necesita una solución rápida, como en gráficos por computadora o en cálculos preliminares. Para mejorar su precisión, se puede usar la regla compuesta del trapecio, que divide el intervalo en múltiples subintervalos.

**Fórmula:**

$$
\int_a^b f(x)\, dx \approx \frac{(b - a)}{2} \left[ f(a) + f(b) \right]
$$


Para un solo intervalo, la fórmula calcula el área del trapecio formado por los puntos $(a, f(a))$ y $(b, f(b))$. En la regla compuesta, se suma el área de varios trapecios pequeños, ajustando los puntos intermedios.

[Ver código de Trapecio](/T4_DiferenciaciónIntegración/Métodos_De_Integración/Trapecio.py)
---



