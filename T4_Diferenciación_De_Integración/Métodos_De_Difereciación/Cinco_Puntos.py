import math

def funcion(x):
    return x * math.sin(x)

def cinco_puntos(x, h):
    # Evaluar la función en los puntos necesarios
    fx1 = funcion(x + 2 * h)
    fx2 = funcion(x + h)
    fx3 = funcion(x - h)
    fx4 = funcion(x - 2 * h)
    
