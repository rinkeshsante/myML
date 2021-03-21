import numpy as np


def getModel(points):
    n = len(points)

    x = 0
    y = 0
    x2 = 0
    y2 = 0
    xy = 0

    sumofProduct = 0
    for p in points:
        x += p[0]
        y += p[1]
        x2 += p[0]**2
        y2 += p[1]**2
        xy += p[0]*p[1]

    # print(x, y, x2, y2, xy)

    m = (n*xy - x*y)/(n*x2 - x**2)
    c = (y*x2 - x*xy)/(n*x2 - x**2)

    return c, m


p = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 3]
]

print(getModel(p))
