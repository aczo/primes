#library of various plots

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
import mpmath as mp
import complexplot as cp
import primes


# vectorize some useful functions
primesbelow = np.vectorize(primes.primesbelow)
li = np.vectorize(mp.li)
RiemannR = np.vectorize(primes.RiemannR)
RiemannPi = np.vectorize(primes.RiemannPi)

def plotgamma():                # gamma function display - auxiliary plot
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

def plotSampleC():              # sample complex plot with hsv coloring
    x = np.arange(-1, 4, 0.05)
    y = np.arange(-1, 3, 0.05)
    x, y = np.meshgrid(x, y)
    z = x + 1j * y
    cp.plotComplex(z, [-1, 4, -1, 3])

def plotPrimeCount():    # prime numbers plot
    x = np.linspace(1, 100, 3000)
    y = RiemannPi(x)
    p = primesbelow(x)
    plt.plot(x, y, 'g', label='R(x)')
    plt.plot(x, p, 'r', label='primes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0, 100])
    plt.ylim([0, 26])
    plt.legend(loc='lower right')
    plt.show()
