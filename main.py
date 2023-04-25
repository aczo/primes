# Prime numbers

import matplotlib.pyplot as plt
import numpy as np
import scipy

# Data for plotting
t = np.linspace(-1.0, 6.0, 1000)
s = scipy.special.gamma(t)

x = np.arange(1, 7, 1)
y = scipy.special.factorial(x-1)

fig, ax = plt.subplots()
ax.plot(t, s, label="Gamma")

ax.plot(x, y, "or", label="(x-1)!")

ax.set(xlabel='x', ylabel='y',
       title='Gamma vs factorial')
ax.legend()
ax.grid()

plt.show()
