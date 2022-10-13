# by Matias I. Bofarull Oddo - 2022.09.19

import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(111)

p = [0, 1, 2]
x = [1, 0, 0]
y = [0, 0, 1]

for i in range(len(p)):
    ax.text(x[i], y[i], "  t" + str(i) + "\n", weight="bold")
ax.scatter(x, y, s=100, c="k", zorder=-1)

t = [-1, 0, +1]

interp_x = []
interp_y = []

for i in range(t[0] * 1000, t[-1] * 1000):
    t = i / 1000
    interp_x.append(((t ** 2) - t) / 2)
    interp_y.append(((t ** 2) + t) / 2)
ax.scatter(
    interp_x,
    interp_y,
    s=5,
    c=range(len(interp_x)),
    cmap="viridis",
)

t = [-1, 0, +2]

interp_x = []
interp_y = []

for i in range(t[0] * 1000, t[-1] * 1000):
    t = i / 1000
    interp_x.append(((t ** 2) - (2 * t)) / 3)
    interp_y.append(((t ** 2) + t) / 6)
ax.scatter(
    interp_x,
    interp_y,
    s=5,
    c=range(len(interp_x)),
    cmap="plasma",
)

t = [-1, 0, +3]

interp_x = []
interp_y = []

for i in range(t[0] * 1000, t[-1] * 1000):
    t = i / 1000
    interp_x.append(((t ** 2) - (3 * t)) / 4)
    interp_y.append(((t ** 2) + t) / 12)
ax.scatter(
    interp_x,
    interp_y,
    s=5,
    c=range(len(interp_x)),
    cmap="inferno",
)

plt.xlim([-0.7, 1.2])
plt.ylim([-0.5, 1.4])

plt.gca().set_position([0, 0, 1, 1])
plt.axis("off")
plt.show()
