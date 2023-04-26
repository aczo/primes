# Prime numbers

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
import complexplot as cp


def plotgamma():
    x = np.linspace(-3.5, 5.5, 2251)
    # Data for plotting
    y = gamma(x)

    plt.plot(x, y, 'b', alpha=0.6, label='gamma(x)')
    k = np.arange(1, 7)
    plt.plot(k, factorial(k-1), 'r*', alpha=0.6, label='(x-1)!, x = 1, 2, ...')
    plt.xlim(-3.5, 5.5)
    plt.ylim(-10, 25)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='lower right')
    plt.show()

def plotSampleC():
    x = np.arange(-1, 4, 0.05)
    y = np.arange(-1, 3, 0.05)
    x, y = np.meshgrid(x, y)
    z = x + 1j * y
    cp.plotComplex(z, [-1, 4, -1, 3])


# plotgamma()
plotSampleC()