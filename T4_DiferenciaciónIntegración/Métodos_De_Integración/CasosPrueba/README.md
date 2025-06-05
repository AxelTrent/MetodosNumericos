# Introducción a los Casos de Prueba
Este proyecto implementa cuatro métodos numéricos. Cada método incluye un caso funcional, que demuestra la precisión de la integración con parámetros válidos, y un caso de error, que verifica el manejo de entradas inválidas o configuraciones que generan excepciones. A continuación, se presenta una breve descripción de cada método, junto con una ventaja y una desventaja específicas.

## 1. Cuadratura Gaussiana (2 puntos)

   - Ventaja: Alta precisión para funciones suaves con pocos puntos, gracias al uso de nodos y pesos óptimos de Gauss-Legendre.
   - Desventaja: Implementación compleja, ya que requiere conocer y transformar los puntos y pesos para el intervalo deseado.

[Ver prueba](/T4_DiferenciaciónIntegración/Métodos_De_Integración/CasosPrueba/CuadraturaGaussiana.md)

## 2. Simpson 1/3

   - Ventaja: Fácil de implementar y ofrece buena precisión para funciones continuas, utilizando una aproximación parabólica.
   - Desventaja: Requiere un número par de segmentos, lo que limita su flexibilidad en ciertos casos.

[Ver prueba](/T4_DiferenciaciónIntegración/Métodos_De_Integración/CasosPrueba/Simpson1_3.md)

## 3. Simpson 3/8

   - Ventaja: Mayor precisión que el método del trapecio para el mismo número de segmentos, debido a su aproximación cúbica.
   - Desventaja: Exige que el número de segmentos sea múltiplo de 3, lo que puede restringir su aplicabilidad.

[Ver prueba](/T4_DiferenciaciónIntegración/Métodos_De_Integración/CasosPrueba/Simpson3_8.md)

## 4. Trapecio

   - Ventaja: Simple de implementar y conceptualmente intuitivo, ya que usa una aproximación lineal entre puntos.
   - Desventaja: Menos preciso que otros métodos como Simpson, especialmente para funciones con alta curvatura.

[Ver prueba](/T4_DiferenciaciónIntegración/Métodos_De_Integración/CasosPrueba/Trapecio.md)
   
Estos casos de prueba garantizan que los métodos sean confiables y manejen adecuadamente tanto escenarios válidos como errores, facilitando su uso en aplicaciones prácticas.
