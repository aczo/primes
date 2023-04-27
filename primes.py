import numpy as np
import mpmath as mp
from scipy.special import factorial, zeta

# constant list of primes below given number - in the range 2 - 100
primes = [0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11,
          11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16,
          16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22,
          23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]


def primesbelow(x):     # returns number of primes smaller than given number (in the range 2..102)
    rv = 0
    if 2 < x < 102:
        rv = primes[int(x-1.0001)]
    return rv


def RiemannR(x):        # implements Riemann R(x) using approximation for first N elements
    N = 20              # assume 20 elements in the approximation
    if x > 0: # 1.0 <= x <=100.0:
        rv = 1
        for i in range(N):  # calculate main part of Rieman R(x)
            k = i + 1
            rv += (np.log(x)**k)/(k*factorial(k)*zeta(k+1))
    else:
        rv=0
    return rv


def RiemannPi(x, zeroes=0):       # approximation of Riemann pi(x) based on R(x) explicit formula
    N = 20              # 20 first terms in approximation
    rv = RiemannR(x)
    for i in range(N):  # correction consivering N trivial zeroes
        rv -= RiemannR(x**(-2.0*(i+1)))
    return rv


def RiemannExplicit(x):
    rv = 0
    if x > 1:
        rv = mp.li(x) - 1/mp.log(x) +1/np.pi*np.arctan(np.pi/np.log(x))
    return rv
