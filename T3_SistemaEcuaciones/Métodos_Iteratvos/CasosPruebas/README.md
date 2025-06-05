# Resolución Numérica con Gauss-Seidel, Jacobi y Método de la Secante

Este proyecto contiene implementaciones en Python de tres métodos numéricos:

1. **Gauss-Seidel** y **Jacobi** para resolver sistemas de ecuaciones lineales
2. **Método de la Secante** para encontrar raíces de ecuaciones no lineales

## Introducción a los Métodos

### Métodos para Sistemas Lineales (Ax = b)

#### Gauss-Seidel
- **Tipo**: Iterativo
- **Características**:
  - Actualiza variables usando valores recién calculados
  - Requiere matriz diagonalmente dominante o simétrica positiva definida
- **Ventaja**: Convergencia más rápida que Jacobi
- **Limitación**: Puede divergir si no se cumplen condiciones de convergencia

 [Ver pruebas de la Gauss-Seidel](/T3_SistemaEcuaciones/Métodos_Iteratvos/CasosPruebas/PruebaGauss_Seidel.md)

#### Jacobi
- **Tipo**: Iterativo
- **Características**:
  - Usa valores completos de la iteración anterior
  - Requiere matriz diagonalmente dominante
- **Ventaja**: Implementación más simple
- **Limitación**: Convergencia más lenta que Gauss-Seidel

 [Ver pruebas de Jacobi](/T3_SistemaEcuaciones/Métodos_Iteratvos/CasosPruebas/PruebaJacobi.md)

### Método para Ecuaciones No Lineales (f(x) = 0)

#### Método de la Secante
- **Tipo**: Iterativo
- **Características**:
  - Usa dos puntos iniciales
  - No requiere cálculo de derivadas
- **Ventaja**: Rápida convergencia para funciones suaves
- **Limitación**: Sensible a elección de puntos iniciales

  [Ver pruebas de la Secante](/T3_SistemaEcuaciones/Métodos_Iteratvos/CasosPruebas/PruebaSecante.md)

## Casos de Prueba

### Casos Exitosos
- **Para Gauss-Seidel/Jacobi**:
  - Sistemas con matrices diagonalmente dominantes
  - Convergencia rápida y estable

- **Para Secante**:
  - Funciones continuas y diferenciables
  - Puntos iniciales adecuados cerca de la raíz

### Casos Fallidos
- **Para Gauss-Seidel/Jacobi**:
  - Matrices no diagonalmente dominantes
  - Sistemas singulares o mal condicionados

- **Para Secante**:
  - Puntos iniciales mal elegidos
  - Funciones con discontinuidades o derivadas problemáticas

## Objetivo del Proyecto
Los casos de prueba permiten:
- Evaluar el comportamiento de cada método
- Identificar condiciones óptimas de aplicación
- Proponer mejoras como:
  - Validaciones automáticas de convergencia
  - Estrategias para selección de parámetros iniciales
  - Manejo de casos especiales

