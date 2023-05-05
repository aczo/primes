# batch optimized processing for multiplot generation
# (c) 2023 aczo

from primes import RiemannR, Ck, Mobius
from numpy import log, pi, arctan
from time import time
from datetime import timedelta


def RiemannPiBatch(xarr, N = 10):    # batch calculation of Riemann R(x) explicit formula, returns array of N outputs
    M = 5      # number of f(x) Ck corrections applied to each R(x) point
    y = [[0 for i in range(len(xarr))] for j in range(N + 1)]
    k = 0

    curr = 0
    total = len(xarr)
    for x in xarr:
        curr += 1
        start = time()
        print("\rProcessing item " + str(curr) + "/" + str(total) + "...", end="", flush=True)
        rv = 0.0
        if x >= 2:
            rv = RiemannR(x) - 1 / log(x) + 1/pi * arctan(pi/log(x))
        y[0][k] = rv
        for i in range(1, N + 1):  # correction considering N non-trivial zeroes
            y[i][k] = y[i - 1][k]
            if x >= 2:
                for j in range(1, M + 1):       # introduce Ck corrections
                    y[i][k] += Mobius(j)/j*Ck((x**(1/j)), i)
        k += 1
        elapsed = time()-start
        etc = (total-curr) * elapsed
        print("done in {:.2f} seconds.".format(elapsed) + " ETC: " + str(timedelta(seconds=int(etc))))
    return y
