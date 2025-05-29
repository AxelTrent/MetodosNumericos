# Métodos para la Resolución de Ecuaciones Diferenciales Ordinarias (EDOs)

Este repositorio contiene implementaciones de distintos métodos numéricos para resolver **Ecuaciones Diferenciales Ordinarias (EDOs)**. Los métodos están organizados en tres categorías:

---

## 📌 Métodos de 1 Paso

Los **métodos de un paso** utilizan únicamente la información del **paso actual** para calcular el siguiente. Son simples, fáciles de implementar y eficientes en muchos casos.

### Archivos en esta carpeta:

- `RungeKutta.py`:  
  Implementa el método de **Runge-Kutta** (típicamente de **orden 4**), uno de los métodos más populares y precisos.  
  - Evalúa la derivada en varios puntos dentro del intervalo.  
  - Ofrece **alta precisión** con un solo paso por iteración.

[Ver Carpeta](/T6_EcuacionesDiferenciales/Metodos_1_Paso/)
---

## 🔁 Métodos de Pasos Múltiples

Los **métodos de pasos múltiples** utilizan información de **varios pasos anteriores** para predecir el siguiente valor.  
Esto mejora la eficiencia al reducir la cantidad de evaluaciones de la función derivada.

### Archivos en esta carpeta:

- `AdamsBashforth.py`:  
  Contiene el método de **Adams-Bashforth**, un método **explícito** de pasos múltiples.  
  - Usa diferencias finitas para aproximar soluciones.  
  - Ideal cuando se desea **mayor precisión con menos evaluaciones**.  
  - Requiere **valores iniciales previos**.
  - 
[Ver Carpeta](/T6_EcuacionesDiferenciales/Metodos_Pasos_Multiples/)
---

## 🔗 Métodos para Sistemas de Ecuaciones

Estos métodos están diseñados para resolver **sistemas de EDOs**, donde múltiples variables están acopladas y evolucionan simultáneamente.

### Archivos en esta carpeta:

- `EulerSystem.py`:  
  Implementa una variante del **método de Euler** adaptada a **sistemas de EDOs**.  
  - Actualiza todas las variables del sistema en cada paso.  
  - Método básico, de **primer orden**, con menor precisión que otros, pero útil para problemas simples o con fines educativos.

[Ver Carpeta](/T6_EcuacionesDiferenciales/Metodos_Sistemas_Ecuaciones/)
---

> 📎 Nota: Los métodos de un paso son más sencillos y directos. Los métodos de pasos múltiples requieren información histórica pero mejoran la eficiencia. Para sistemas, es fundamental considerar el acoplamiento de variables.

