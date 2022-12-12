import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

plt.rcParams['backend'] = 'Qt5Agg'
plt.rcParams['toolbar'] = 'None'

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(0, 1, 0.05)
Y = np.arange(0, 1, 0.05)
X, Y = np.meshgrid(X, Y)
Z = X + Y

mngr = plt.get_current_fig_manager()
_, _, dx, dy = mngr.window.geometry().getRect()
ax.plot_surface(X, Y, Z, linewidth=0, cmap=cm.coolwarm)
plt.show()

