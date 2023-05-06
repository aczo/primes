# Implementation of various plots

import numpy as np
import primes
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# vectorize functions that are referred to in plots
Pi = np.vectorize(primes.Pi)
RiemannPi = np.vectorize(primes.RiemannPi)
Ck = np.vectorize(primes.Ck)


def plotCk(k):                         # plots Ck(i)
    x = np.linspace(2, 100, 3000)
    c = Ck(x, k)
    plt.plot(x, c, 'b')
    plt.show()


def plotPrimeCount(n = 0):    # prime numbers plot, with N being number of zeta zeros to include in R(x) correction
    xp = np.linspace(0, 100, 10000)
    p = Pi(xp)
    x = np.linspace(1, 100, 1920)
    y = RiemannPi(x, n)

    px = 1 / plt.rcParams['figure.dpi']
    figure, axis = plt.subplots(2, 1, figsize=(1920*px, 1080*px))
    figure.suptitle(r"Approximation of prime counting function $\pi(x)$ by Riemann's R(x)", fontsize=14)
    plt.subplots_adjust(left=0.06, right=0.94, top=0.9, bottom=0.03, wspace=0.07, hspace=0.15)
    axis[0].plot(xp, p, 'r', label=r'$\pi(x)$', linewidth=2)
    axis[0].plot(x, y, 'g', label='R(x)', linewidth=2)
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
    axis[1].plot(xp, p, 'r', label=r'$\pi(x)$', linewidth=2)
    axis[1].plot(x, y, 'g', label='R(x)', linewidth=2)
    axis[1].set_label('x')
    axis[1].set_label('y')
    axis[1].set_title("0 < x < 20")
    axis[1].set_xlim([0, 20])
    axis[1].set_ylim([0, 8.5])
    axis[1].xaxis.set_major_locator(MultipleLocator(5))
    axis[1].xaxis.set_major_formatter('{x:.0f}')
    axis[1].xaxis.set_minor_locator(MultipleLocator(1))
    axis[1].legend(loc='lower right')
    figure.text(0.4, 0.94, str(n) + r" non-trivial $\zeta$ zeros corrections included", fontsize=14)
    figure.text(0.97, 0.98, r"ac, 2023", fontsize=8)
    return plt


def plotSinglePrimeCount(x, yarr, n = 0):    # prime numbers single plot (no zoom), with N being number of zeta zeros to include in R(x) correction
    xp = np.linspace(0, 100, 10000)
    p = Pi(xp)

    px = 1 / plt.rcParams['figure.dpi']
    figure, axis = plt.subplots(1, 1, figsize=(1080*px, 1920*px))
    figure.suptitle(r"Approximation of prime counting function $\pi(x)$ by Riemann's R(x)")
    axis.plot(xp, p, 'r', label=r'$\pi(x)$', linewidth=2)
    axis.plot(x, yarr[n], 'g', label='R(x)', linewidth=2)
    axis.set_label('x')
    axis.set_label('y')
    axis.set_title("0 < x < 100")
    axis.set_xlim([0, 100])
    axis.set_ylim([0, 26])
    axis.xaxis.set_major_locator(MultipleLocator(10))
    axis.xaxis.set_major_formatter('{x:.0f}')
    axis.xaxis.set_minor_locator(MultipleLocator(1))
    axis.yaxis.set_minor_locator(MultipleLocator(1))
    axis.legend(loc='lower right')
    figure.text(0.4, 0.93, str(n) + r" non-trivial $\zeta(x)$ zeros corrections included", fontsize=12)
    return plt
