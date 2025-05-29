Los métodos de pasos múltiples utilizan información de **varios pasos anteriores** para predecir el siguiente valor.  
Esto mejora la eficiencia al reducir la cantidad de evaluaciones de la función derivada.

### 📂 Archivos en esta carpeta:

- `AdamsBashforth.py`:  
  Contiene el método de **Adams-Bashforth**, un método **explícito** de pasos múltiples.

### 📐 Fórmula de Adams-Bashforth de 2 pasos:

$$
y_{n+1} = y_n + \frac{h}{2} \left[3f(t_n, y_n) - f(t_{n-1}, y_{n-1})\right]
$$

- Usa diferencias finitas para aproximar soluciones.  
- Ideal cuando se desea **mayor precisión con menos evaluaciones**.  
- Requiere **valores iniciales previos**.

