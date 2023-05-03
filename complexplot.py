# Plots complex plane for given data using Hue-Saturation-Value coloring. Currently not used
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def g(x):                   # auxiliary function - reducing gradient to present colors better
    return (1 - 1/(1+x**2))**0.2


def calcHue(z):            # auxiliary function - computes the hue corresponding to the complex number z based on its argument
    h = np.angle(z) / (2*np.pi)
    return np.mod(h, 1)


def plotComplex(z, e):      # plots complex function given by mesh z with given extent coordinates
    h = calcHue(z)
    v = g(np.absolute(z))
    s = 0.9 * np.ones(h.shape)
    hsv = np.dstack((h, s, v))
    rgb = mcolors.hsv_to_rgb(hsv)
    plt.imshow(rgb, origin="lower", extent=e)
    plt.show()
