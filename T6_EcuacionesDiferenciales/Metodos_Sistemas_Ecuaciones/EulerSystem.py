def f(x, y1, y2):
    # Retorna las derivadas dy1/dx y dy2/dx como una lista
    dy1 = -2 * x * y1       # dy1/dx
    dy2 = y1 - y2           # dy2/dx
    return [dy1, dy2]

