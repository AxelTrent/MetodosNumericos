Los métodos de un paso utilizan únicamente la información del **paso actual** para calcular el siguiente.  
Son simples, fáciles de implementar y eficientes en muchos casos.

### 📂 Archivos en esta carpeta:

- `RungeKutta.py`:  
  Implementa el método de **Runge-Kutta** (típicamente de **orden 4**), uno de los métodos más populares y precisos.

### 📐 Fórmula del método Runge-Kutta de orden 4:

$$
y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)
$$

donde:

$$
k_1 = f(t_n, y_n) \\
k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right) \\
k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right) \\
k_4 = f(t_n + h, y_n + hk_3)
$$

Este método evalúa la derivada en varios puntos dentro del intervalo.  
Ofrece **alta precisión** con un solo paso por iteración.
