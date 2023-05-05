# Main function
# (c) 2023 aczo

from plots import plotPrimeCount

import argparse
from time import time
from datetime import timedelta


def parse_range(astr):
    result = set()
    for part in astr.split(','):
        x = part.split('-')
        result.update(range(int(x[0]), int(x[-1]) + 1))
    return sorted(result)


parser = argparse.ArgumentParser(description = "Generates plots of Riemann R(x) with specified number of zeta zeroes corrections")
parser.add_argument('zeroes', type=parse_range, help='List of plots with given numbers of zeta zeroes, e.g. 1,2,4-8')
args = parser.parse_args()
print(args.zeroes)

for z in args.zeroes:
    print("Generating plot for " + str(z) + " non-trivial zeroes...", end="", flush=True)
    start = time()
    plt = plotPrimeCount(z)
    print("done. Time elapsed: " + str(timedelta(seconds=time()-start)))
    plt.savefig("R_x_{:03d}".format(z) + ".png")
    plt.close()

