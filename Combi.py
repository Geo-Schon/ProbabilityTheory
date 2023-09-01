from math import factorial
import numpy as np


def combinations(i, j):
    return int(factorial(i) / (factorial(j) * factorial(i - j)))


def combination(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))
