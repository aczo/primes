# Main function
from time import time
from datetime import timedelta
from plots import plotPrimeCount


for z in range(2):
    print("Generating plot for " + str(z) + " trivial zeroes...", end="", flush=True)
    start = time()
    plt = plotPrimeCount(z)
    print("done. Time elapsed: " + str(timedelta(seconds=time()-start)))
    plt.savefig("R_x_{:03d}".format(z) + ".png")