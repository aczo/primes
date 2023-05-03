from numpy import abs, log, pi, arctan, cos
from cmath import phase
import mpmath as mp


from scipy.special import factorial, zeta, expi

# constant list of primes below given number - in the range 2 - 100
primes = [0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11,
          11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16,
          16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22,
          23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]

firstprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def primesbelow(x):     # returns number of primes smaller than given number (in the range 2..102)
    rv = 0.0
    if 2 < x < 102:
        rv = primes[int(x-1.0001)]
    return rv


def RiemannR(x):        # implements Riemann R(x) using approximation for first N elements
    N = 20              # assume 20 elements in the approximation
    rv = 0.0
    if x == 2:
        rv = 0.5
    if x > 2:
        rv = 1.0
        for i in range(1, N + 1):  # calculate main part of Riemann R(x)
            rv += (log(x)**i)/(i*factorial(i)*zeta(i+1))
    return rv


def RiemannPi(x, N = 0):       # approximation of Riemann pi(x) based on R(x) explicit formula, N - number of zeta zeroes to consider
    rv = 0.0
    if x >= 2:
        rv = RiemannR(x) - 1 / log(x) + 1/pi * arctan(pi/log(x))
        for i in range(1, N + 1):  # correction considering N non-trivial zeroes
            rho = complex(mp.zetazero(i))
            # below's R(x) correction based on Hans Riesel formula for a pair of complex conjugate zeta zeroes
            rv -= 2 * x ** (1 / 2) / abs(rho) / log(x) * cos(rho.imag * log(x) - phase(rho))
    return rv
