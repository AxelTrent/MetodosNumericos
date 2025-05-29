Los métodos de diferenciación numérica permiten aproximar la derivada de una función en un punto dado usando valores discretos de la función. Esto es útil cuando no se puede obtener la derivada analíticamente o cuando se trabaja con datos experimentales. A continuación, se describen los métodos incluidos con mayor detalle:

Cinco Puntos
El método de cinco puntos es una técnica avanzada para aproximar la primera derivada de una función en un punto, utilizando cinco valores de la función en puntos igualmente espaciados. Este método es conocido por su alta precisión, ya que reduce el error de truncamiento al usar una combinación ponderada de los puntos. Es especialmente útil en problemas donde se necesita una estimación precisa de la derivada, como en simulaciones físicas o análisis de señales. La fórmula central de cinco puntos considera dos puntos a la izquierda y dos a la derecha del punto de interés, lo que lo hace más robusto frente a pequeñas variaciones en los datos.

Fórmula (fórmula central de cinco puntos):

𝑓
′
(
𝑥
0
)
≈
−
𝑓
(
𝑥
0
+
2
ℎ
)
+
8
𝑓
(
𝑥
0
+
ℎ
)
−
8
𝑓
(
𝑥
0
−
ℎ
)
+
𝑓
(
𝑥
0
−
2
ℎ
)
12
ℎ
f 
′
 (x 
0
​
 )≈ 
12h
−f(x 
0
​
 +2h)+8f(x 
0
​
 +h)−8f(x 
0
​
 −h)+f(x 
0
​
 −2h)
​
 
Donde 
ℎ
h es el tamaño del paso entre los puntos, y 
𝑥
0
x 
0
​
  es el punto donde se calcula la derivada. El denominador 
12
ℎ
12h y los coeficientes 
−
1
,
8
,
−
8
,
1
−1,8,−8,1 aseguran que el error de truncamiento sea del orden de 
ℎ
4
h 
4
 , lo que lo hace mucho más preciso que métodos más simples.

Tres Puntos
El método de tres puntos es una técnica más sencilla para calcular derivadas numéricas, utilizando solo tres valores de la función: uno en el punto de interés y uno a cada lado. Aunque es menos preciso que el método de cinco puntos (con un error de truncamiento del orden de 
ℎ
2
h 
2
 ), es más rápido y fácil de implementar, lo que lo hace ideal para problemas donde la precisión no es crítica o los datos son ruidosos. Este método se usa frecuentemente en aplicaciones iniciales de análisis numérico, como en la enseñanza o en simulaciones preliminares. La fórmula central de tres puntos es simétrica y simple, lo que facilita su aplicación.

Fórmula (fórmula central de tres puntos):

𝑓
′
(
𝑥
0
)
≈
𝑓
(
𝑥
0
+
ℎ
)
−
𝑓
(
𝑥
0
−
ℎ
)
2
ℎ
f 
′
 (x 
0
​
 )≈ 
2h
f(x 
0
​
 +h)−f(x 
0
​
 −h)
​
 
Aquí, 
ℎ
h es el tamaño del paso, y la fórmula mide la diferencia entre los valores de la función a la derecha y a la izquierda del punto 
𝑥
0
x 
0
​
 , dividiendo por el doble del paso para obtener la pendiente aproximada.

