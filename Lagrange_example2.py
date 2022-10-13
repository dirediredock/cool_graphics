# by Matias I. Bofarull Oddo - 2022.09.19

import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(111)  # projection="3d", proj_type="ortho")

t = [0, 1, 2, 3]
x = [-1, 0, 0, +1]
y = [0, 0, +1, +1]

for i in range(len(t)):
    ax.text(x[i], y[i], "  t" + str(i), weight="bold")
ax.scatter(x, y, s=50, c="darkslateblue", zorder=10)

interp_x = []
interp_y = []

for i in range(t[0] * 1000, t[-1] * 1000):
    t = i / 1000
    interp_x.append(((t ** 3) / 3) + ((3 * (t ** 2)) / -2) + ((13 * t) / 6) - 1)
    interp_y.append(((t ** 3) / -3) + ((3 * (t ** 2)) / 2) + ((7 * t) / -6))

plt.scatter(interp_x, interp_y, s=50, c=range(len(interp_x)), cmap="inferno")

plt.axis("off")
plt.show()
