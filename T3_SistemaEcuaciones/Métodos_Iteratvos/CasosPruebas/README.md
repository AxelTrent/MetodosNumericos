# Resolución de Sistemas de Ecuaciones Lineales: Eliminación Gaussiana, Gauss-Seidel y Jacobi

Este proyecto contiene implementaciones en Python de tres métodos numéricos para resolver sistemas de ecuaciones lineales: Eliminación Gaussiana, Gauss-Seidel y Jacobi. Cada método aborda el problema de encontrar soluciones para sistemas de la forma Ax = b, donde A es la matriz de coeficientes y b es el vector de términos independientes.

## Introducción a los Métodos y Casos de Prueba

### Eliminación Gaussiana
- **Tipo**: Método directo
- **Proceso**:
  1. Transforma la matriz aumentada en forma triangular superior mediante operaciones de fila
  2. Realiza sustitución hacia atrás para obtener las soluciones
- **Fortalezas**: Robusto para sistemas no singulares
- **Limitaciones**: Falla en matrices con pivotes nulos o singularidades

### Gauss-Seidel
- **Tipo**: Método iterativo
- **Características**:
  - Actualiza variables en cada iteración usando los valores más recientes
  - Requiere matriz diagonalmente dominante o simétrica positiva definida para convergencia
- **Ventaja**: Generalmente más rápido que Jacobi
- **Riesgo**: Puede diverger si no se cumplen las condiciones de convergencia

### Jacobi
- **Tipo**: Método iterativo
- **Características**:
  - Utiliza valores de la iteración anterior para todas las variables
  - Requiere matriz diagonalmente dominante para converger
- **Ventaja**: Implementación más simple
- **Desventaja**: Convergencia más lenta que Gauss-Seidel

## Casos de Prueba Diseñados

### Casos Exitosos
- Sistemas con matrices:
  - Diagonalmente dominantes (para métodos iterativos)
  - No singulares (para eliminación gaussiana)
- Garantizan:
  - Convergencia (métodos iterativos)
  - Soluciones exactas (eliminación gaussiana)

### Casos Fallidos
- Sistemas con matrices:
  - Singulares
  - No diagonalmente dominantes
  - Mal condicionados
- Provocan:
  - Errores de división por cero
  - Falta de convergencia
  - Resultados numéricamente inestables

## Objetivo de los Casos de Prueba
Estos casos ilustran:
- Las fortalezas y limitaciones de cada método
- La importancia de validar las condiciones de aplicación
- Posibles mejoras como:
  - Implementación de pivoteo
  - Validaciones de convergencia
  - Manejo de casos especiales

