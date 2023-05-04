# batch optimized processing for multiplot generation
# (c) 2023 aczo

from primes import RiemannR
from mpmath import zetazero
from numpy import abs, log, pi, arctan, cos, sqrt
from cmath import phase
from time import time


def RiemannPiBatch(xarr, N = 10):    # batch calculation of Riemann pi(x) based on R(x) explicit formula, returns array of N outputs
    y = [[0 for i in range(len(xarr))] for j in range(N + 1)]
    k = 0

    for x in xarr:
        start = time()
        print("Processing value x: " + str(x) + "...", end="", flush=True)
        rv = 0.0
        if x >= 2:
            rv = RiemannR(x) - 1 / log(x) + 1/pi * arctan(pi/log(x))
        y[0][k] = rv
        for i in range(1, N + 1):  # correction considering N non-trivial zeroes
            if x >= 2:
                rho = complex(zetazero(i))
                # below's R(x) correction based on Hans Riesel formula for a pair of complex conjugate zeta zeroes
                y[i][k] = y[i-1][k] - 2 * sqrt(x) * cos(rho.imag * log(x) - phase(rho)) / abs(rho) / log(x)
            else:
                y[i][k] = y[i-1][k]
        k += 1
        print("done. Time elapsed: " + str(time()-start))
    return y
