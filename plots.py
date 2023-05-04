# Implementation of various plots

import numpy as np
import primes
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# vectorize functions that are referred to in plots
Pi = np.vectorize(primes.Pi)
RiemannPi = np.vectorize(primes.RiemannPi)


def plotPrimeCount(x, yarr, n = 0):    # prime numbers plot, with N being number of zeta zeros to include in R(x) correction
    xp = np.linspace(0, 100, 10000)
    p = Pi(xp)

    px = 1 / plt.rcParams['figure.dpi']
    figure, axis = plt.subplots(2, 1, figsize=(1920*px, 1080*px))
    figure.suptitle(r"Approximation of prime counting function $\pi(x)$ by Riemann's R(x)")
    plt.subplots_adjust(left=0.06, right=0.94, top=0.9, bottom=0.03, wspace=0.07, hspace=0.15)
    axis[0].plot(xp, p, 'r', label=r'$\pi(x)$', linewidth=1.5)
    axis[0].plot(x, yarr[n], 'g', label='R(x)', linewidth=1.5)
    axis[0].set_label('x')
    axis[0].set_label('y')
    axis[0].set_title("0 < x < 100")
    axis[0].set_xlim([0, 100])
    axis[0].set_ylim([0, 26])
    axis[0].xaxis.set_major_locator(MultipleLocator(10))
    axis[0].xaxis.set_major_formatter('{x:.0f}')
    axis[0].xaxis.set_minor_locator(MultipleLocator(1))
    axis[0].yaxis.set_minor_locator(MultipleLocator(1))
    axis[0].legend(loc='lower right')
    axis[1].plot(xp, p, 'r', label=r'$\pi(x)$', linewidth=1.5)
    axis[1].plot(x, yarr[n], 'g', label='R(x)', linewidth=1.5)
    axis[1].set_label('x')
    axis[1].set_label('y')
    axis[1].set_title("0 < x < 20")
    axis[1].set_xlim([0, 20])
    axis[1].set_ylim([0, 8.5])
    axis[1].xaxis.set_major_locator(MultipleLocator(5))
    axis[1].xaxis.set_major_formatter('{x:.0f}')
    axis[1].xaxis.set_minor_locator(MultipleLocator(1))
    axis[1].legend(loc='lower right')
    figure.text(0.4, 0.93, str(n) + r" non-trivial $\zeta(x)$ zeros corrections included", fontsize=12)
    return plt
