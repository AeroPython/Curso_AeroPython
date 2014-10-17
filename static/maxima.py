# Advanced Scientific Programming in Python, autumn school, Trento, 2010
# Day 1, Exercise 1 (unit testing and coverage)
# Author: Pietro Berkes <berkes _at_ brandeis _dot_ edu>


def find_maxima(x):
    """Halla los índices de los máximos relativos"""
    idx = []
    N = len(x)
    if x[1] < x[0]:
        idx.append(0)
    for i in range(1, N - 1):
        if x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)
    if x[-2] < x[-1]:
        idx.append(N - 1)
    return idx
