# Casos de Prueba para Métodos de Resolución de Sistemas Lineales

## Descripción del Proyecto
Este proyecto contiene dos implementaciones en Python para resolver sistemas de ecuaciones lineales:
1. **Eliminación Gaussiana**   
2. **Método de Gauss-Jordan**    
Los casos de prueba están diseñados para evaluar el comportamiento de ambos algoritmos en diferentes escenarios.

## Introducción a los Casos de Prueba

### Objetivos
- Validar la funcionalidad de los algoritmos en escenarios representativos
- Identificar condiciones que afectan su desempeño
- Comprender las limitaciones de los métodos implementados

### Tipos de Casos
1. **Caso Exitoso**: 
   - Sistema con matriz no singular (determinante ≠ 0)
   - Garantiza solución única
   - Pivotes no nulos durante el proceso

2. **Caso Fallido**:
   - Sistema con matriz singular o inconsistente
   - Puede provocar errores (división por cero)
   - Presenta dependencias lineales entre ecuaciones

## Beneficios de los Casos de Prueba
- Permiten comprender las limitaciones de los algoritmos
- Detectan falta de manejo de sistemas singulares/inconsistentes
- Sirven como base para futuras mejoras:
  - Implementación de pivoteo parcial
  - Detección de casos especiales
  - Manejo de sistemas indeterminados
 ---
   [Ver pruebas de Eliminación Gaussiana](/T3_SistemaEcuaciones/Métodos_Directos/CasosPrueba/PruebaEliminacionGaussiana.md)
   
   ---
   [Ver pruebas de Gauss-Jordan](/T3_SistemaEcuaciones/Métodos_Directos/CasosPrueba/PruebaGauss-Jordam.md)

