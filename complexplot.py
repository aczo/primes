# plots complex plane for given data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def g(x):
    return (1 - 1/(1+x**2))**0.2


def Hcomplex(z):            # computes the hue corresponding to the complex number z
    h = np.angle(z) / (2*np.pi)
    return np.mod(h, 1)


def plotComplex(z, e):      # plots complex function with argument and modulus coloring on a 2D plane
    h = Hcomplex(z)
    v = g(np.absolute(z))
    s = 0.9 * np.ones(h.shape)
    hsv = np.dstack((h, s, v))
    rgb = mcolors.hsv_to_rgb(hsv)
    plt.imshow(rgb, origin="lower", extent=e)
    plt.show()
