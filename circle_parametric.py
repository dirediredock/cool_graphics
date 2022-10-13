# by Matias I. Bofarull Oddo - 2022.10.05

import matplotlib.pyplot as plt

from math import sin, cos, pi

fig = plt.gcf()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(111)

interp_x = []
interp_y = []

for i in range(0, round(2 * pi * 1000)):
    t = i / 1000
    interp_x.append(sin(t))
    interp_y.append(cos(t))

plt.scatter(
    interp_x,
    interp_y,
    s=500,
    c=range(len(interp_x)),
    cmap="viridis",
)

plt.show()
