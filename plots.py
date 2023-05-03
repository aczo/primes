# Implementation of various plots

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
import complexplot as cp
import primes


# vectorize functions that are referred to in plots
primesbelow = np.vectorize(primes.primesbelow)
RiemannPi = np.vectorize(primes.RiemannPi)


def plotgamma():                # gamma function display - auxiliary plot
    x = np.linspace(-3.5, 5.5, 2251)
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


def plotPrimeCount(N = 0):    # prime numbers plot, with N being number of zeta zeros to include in R(x) correction
    x = np.linspace(1, 100, 3000)
    y = RiemannPi(x)
    p = primesbelow(x)

    px = 1 / plt.rcParams['figure.dpi']
    figure, axis = plt.subplots(1, 2, figsize=(1920*px, 1080*px))
    figure.suptitle("Approximation of prime counting function by Riemann's pi(x)")
    plt.subplots_adjust(left=0.03, right=0.97, top=0.9, bottom=0.03, wspace=0.07, hspace=0.05)
    axis[0].plot(x, y, 'g', label='R(x)')
    axis[0].plot(x, p, 'r', label='primes')
    axis[0].set_label('x')
    axis[0].set_label('y')
    axis[0].set_title("0 < x < 100")
    axis[0].set_xlim([0, 100])
    axis[0].set_ylim([0, 26])
    axis[0].legend(loc='lower right')
    axis[1].plot(x, y, 'g', label='R(x)')
    axis[1].plot(x, p, 'r', label='primes')
    axis[1].set_label('x')
    axis[1].set_label('y')
    axis[1].set_title("10 < x < 20")
    axis[1].set_xlim([10, 20])
    axis[1].set_ylim([3.5, 8.5])
    axis[1].legend(loc='lower right')
    figure.text(0.43, 0.93, str(N) + " non-trivial Zeta zeros corrections included")
    return plt
    # plt.show()


def plotSampleC():              # sample complex plot with hsv coloring
    x = np.arange(-1, 4, 0.05)
    y = np.arange(-1, 3, 0.05)
    x, y = np.meshgrid(x, y)
    z = x + 1j * y
    cp.plotComplex(z, [-1, 4, -1, 3])
