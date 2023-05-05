# Main function
# (c) 2023 aczo

from plots import plotPrimeCount, plotSinglePrimeCount
import numpy as np
from processor import RiemannPiBatch


N = 10      # number of plots to generate

x = np.linspace(1, 100, 1920)
y = RiemannPiBatch(x, N)
for i in range(N+1):
    plt = plotPrimeCount(x, y, i)
    plt.savefig("R_x_{:03d}".format(i) + ".png")
    print("Saved plot " + str(i+1) + "/" + str(N+1))
    plt.close()

# from plots import plotCk
# plotCk(1)