Métodos Directos
Estos métodos encuentran la solución exacta (dentro de la precisión numérica) en un número finito de pasos. Se basan en transformar el sistema de ecuaciones para resolverlo directamente.

Eliminación Gaussiana
Descripción:
Convierte el sistema de ecuaciones en una matriz triangular superior usando operaciones elementales (como intercambiar filas, multiplicar por un escalar o sumar múltiplos de filas). Luego, se resuelve el sistema por sustitución hacia atrás, empezando desde la última ecuación hacia la primera.

Fórmula:

𝑥
𝑖
=
𝑏
𝑖
−
∑
𝑗
=
1
𝑖
−
1
𝑎
𝑖
𝑗
𝑥
𝑗
𝑎
𝑖
𝑖
,
𝑖
=
𝑛
,
𝑛
−
1
,
.
.
.
,
1
x 
i
​
 = 
a 
ii
​
 
b 
i
​
 −∑ 
j=1
i−1
​
 a 
ij
​
 x 
j
​
 
​
 ,i=n,n−1,...,1
Gauss-Jordan
Descripción:
Es una extensión del método de Gauss. No se detiene al obtener la forma triangular superior, sino que sigue transformando hasta que se obtiene la matriz identidad, lo que permite leer directamente las soluciones sin sustitución.

Fórmula:

𝑥
𝑖
=
𝑏
𝑖
−
∑
𝑗
=
1
,
𝑗
≠
𝑖
𝑛
𝑎
𝑖
𝑗
𝑥
𝑗
𝑎
𝑖
𝑖
x 
i
​
 = 
a 
ii
​
 
b 
i
​
 −∑ 
j=1,j

=i
n
​
 a 
ij
​
 x 
j
​
 
​
 
Métodos Iterativos
Estos métodos aproximan la solución comenzando con un valor inicial y mejorándolo en cada iteración. Se repiten hasta que la diferencia entre iteraciones es lo suficientemente pequeña.

Gauss-Seidel
Descripción:
Usa los valores más recientes calculados dentro de la misma iteración. Esto hace que, en muchos casos, converja más rápido que Jacobi.

Fórmula:

𝑥
𝑖
(
𝑘
+
1
)
=
𝑏
𝑖
−
∑
𝑗
=
1
𝑖
−
1
𝑎
𝑖
𝑗
𝑥
𝑗
(
𝑘
+
1
)
−
∑
𝑗
=
𝑖
+
1
𝑛
𝑎
𝑖
𝑗
𝑥
𝑗
(
𝑘
)
𝑎
𝑖
𝑖
x 
i
(k+1)
​
 = 
a 
ii
​
 
b 
i
​
 −∑ 
j=1
i−1
​
 a 
ij
​
 x 
j
(k+1)
​
 −∑ 
j=i+1
n
​
 a 
ij
​
 x 
j
(k)
​
 
​
 
Jacobi
Descripción:
Cada variable se actualiza usando únicamente los valores de la iteración anterior. No se usan los nuevos valores hasta que termine la iteración, lo que hace que sea más fácil de implementar, pero puede requerir más iteraciones para converger.

Fórmula:

𝑥
𝑖
(
𝑘
+
1
)
=
𝑏
𝑖
−
∑
𝑗
=
1
,
𝑗
≠
𝑖
𝑛
𝑎
𝑖
𝑗
𝑥
𝑗
(
𝑘
)
𝑎
𝑖
𝑖
x 
i
(k+1)
​
 = 
a 
ii
​
 
b 
i
​
 −∑ 
j=1,j

=i
n
​
 a 
ij
​
 x 
j
(k)
​
 
​
 
