# prime number functions
# (c) 2023 aczo

from numpy import abs, log, pi, arctan, cos, sqrt
from cmath import phase
from mpmath import zetazero


from scipy.special import factorial, zeta

# constant list of primes below given number - in the range 2 - 100
primeCount = [0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11,
              11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16,
              16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22,
              23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]


mobius = [1, -1, -1,  0, -1,  1, -1,  0,  0,  1, -1,  0, -1,  1,  1,  0, -1,  0, -1, 0,  1,  1, -1,  0,  0,  1,
          0,  0, -1, -1, -1,  0,  1,  1,  1,  0, -1,  1, 1,  0, -1, -1, -1,  0,  0,  1, -1,  0,  0,  0,  1,  0,
          -1,  0,  1,  0,  1, 1, -1,  0, -1,  1,  0,  0,  1, -1, -1,  0,  1, -1, -1,  0, -1,  1,  0,  0, 1, -1,
          -1,  0,  0,  1, -1,  0,  1,  1,  1,  0, -1,  0,  1,  0,  1,  1,  1, 0, -1,  0,  0,  0, -1, -1, -1,  0,
          -1,  1, -1,  0, -1, -1,  1,  0, -1, -1, 1,  0,  0,  1,  1,  0,  0,  1,  1,  0,  0,  0, -1,  0,  1, -1,
          -1,  0,  1, 1,  0,  0, -1, -1, -1,  0,  1,  1,  1,  0,  1,  1,  0,  0, -1,  0, -1,  0, 0, -1,  1,  0,
          -1,  1,  1,  0,  1,  0, -1,  0, -1,  1, -1,  0,  0, -1,  0, 0, -1, -1,  0,  0,  1,  1, -1,  0, -1, -1,
          1,  0,  1, -1,  1,  0,  0, -1, -1,  0, -1,  1, -1,  0, -1,  0, -1,  0,  1,  1,  1,  0,  1,  1,  0,  0,
          1, 1, -1,  0,  1,  1,  1,  0,  1,  1,  1,  0,  1, -1, -1,  0,  0,  1, -1,  0, -1, -1, -1,  0, -1,  0,
          1,  0,  1, -1, -1,  0, -1,  0,  0,  0,  0, -1,  1, 0,  1,  0, -1,  0,  1,  1, -1,  0, -1, -1,  1,  0,
          0,  1, -1,  0,  1, -1, 1,  0, -1,  0, -1,  0, -1,  1,  0,  0, -1,  1,  0,  0, -1, -1, -1,  0, -1, -1,
          1,  0,  0, -1,  1,  0, -1,  0,  1,  0,  0,  1,  1,  0,  1,  1,  1,  0, 1,  0, -1,  0,  1, -1, -1,  0,
          -1,  1,  0,  0, -1, -1,  1,  0,  1, -1,  1, 0,  0,  1,  1,  0,  1,  1, -1,  0,  0,  1,  1,  0, -1,  0,
          1,  0,  1,  0, 0,  0, -1,  1, -1,  0, -1,  0,  0,  0, -1, -1,  1,  0, -1,  1, -1,  0,  0, 1,  0,  0,
          1, -1, -1,  0,  0, -1,  1,  0, -1, -1,  0,  0,  1,  0, -1,  0, 1,  1, -1,  0, -1,  1,  0,  0, -1,  1,
          1,  0,  1,  1,  1,  0, -1,  1, -1]


zetacache={}


def zetaz(n):           # caches zeta zeroes
    if n in zetacache:
        rv = zetacache[n]
    else:
        print("calculating and caching zeta zero " + str(n) + "...", end="", flush=True)
        rv = complex(zetazero(n))
        zetacache[n] = rv
    return rv


def Mobius(x):          # implements mobius function
    rv = 0
    if 0 < x < 400:
        rv = mobius[x-1]
    return rv


def Pi(x):     # returns number of primes smaller than given number (in the range 2..102)
    rv = 0.0
    if 2 < x < 102:
        rv = primeCount[int(x-1.0001)]
    return rv


def RiemannR(x):        # implements Riemann R(x) using approximation for first N elements
    N = 20              # assume 20 elements in the approximation
    rv = 0.0
    if x >= 2:
        rv = 1.0
        for i in range(1, N + 1):  # calculate main part of Riemann R(x)
            rv += (log(x)**i)/(i*factorial(i)*zeta(i+1))
    return rv


def RiemannPi(x, N = 0):       # approximation of Riemann pi(x) based on R(x) explicit formula, N - number of zeta zeroes to consider
    M = 7      # number of f(x) Ck corrections applied to each R(x) point
    rv = 0.0
    if x >= 2:
        rv = RiemannR(x) - 1 / log(x) + 1/pi * arctan(pi/log(x))
        for i in range(1, N + 1):  # correction considering N non-trivial zeroes
            # below's R(x) correction based on Hans Riesel formula for a pair of complex conjugate zeta zeroes
            for k in range(1, M + 1):  # introduce Ck corrections
                rv += Mobius(k) / k * Ck((x ** (1 / k)), i)
    return rv


def Ck(x, n):              # correction of R(x) resulting from Nth pair of complex zeta zeros
    rho = zetaz(n)
    # R(x) correction based on Hans Riesel formula for a pair of complex conjugate zeta zeroes
    return - 2 * sqrt(x) * cos(rho.imag * log(x) - phase(rho)) / abs(rho) / log(x)
