import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cylinder
x = np.linspace(-1, 1, 100)
z = np.linspace(0, 1, 100)
Xc, Zc = np.meshgrid(x, z)
Yc = np.sqrt(1 - Xc ** 2)

# Draw parameters
rstride = 20
cstride = 10
ax.plot_surface(Xc, Yc, Zc, alpha=0.2)
ax.plot_surface(Xc, -Yc, Zc, alpha=0.2)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()