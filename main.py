# Prime numbers

import matplotlib.pyplot as plt
import numpy as np
import scipy

# Data for plotting
t = np.arange(0.0, 6.0, 0.05)
s = scipy.special.gamma(t+1)

x = np.arange(0, 6, 1)
y = scipy.special.factorial(x)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.plot(x, y, "or")

ax.set(xlabel='x', ylabel='y',
       title='Gamma vs factorial')
ax.grid()

plt.show()
