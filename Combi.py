from math import factorial


def combinations(i, j):
    return int(factorial(i) / (factorial(j) * factorial(i - j)))
