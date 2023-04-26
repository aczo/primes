import numpy as np
from scipy.special import factorial, zeta

primes = [0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]


def primesbelow(x):     # returns number of primes smaller than given number (in the range 2..102)
    rv = 0
    if x > 2 and x < 102:
        rv = primes[int(x-1.0001)]
    return rv


def RiemannR(x):       # implements Riemann R(x) explicit formula approximation for first N elements
    N = 20      # assume 20 elements in the approximation
    rv = 1
    for i in range(N):
        k = i + 1
        rv += (np.log(x)**k)/(k*factorial(k)*zeta(k+1))
    return rv