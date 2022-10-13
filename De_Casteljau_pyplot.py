# by Matias I. Bofarull Oddo - 2022.10.13

from random import randint
import matplotlib.pyplot as plt


def De_Casteljau(points, t):
    point_array = [point for point in points]
    for i in range(1, len(point_array)):
        for m in range(len(point_array) - i):
            point_array[m] = point_array[m] * (1 - t) + point_array[m + 1] * t
    return point_array[0]


x = [0, 0, 4, 9, 8, 9, 7, 2, 7, 1]
y = [0, 9, 8, 9, 8, 0, 1, 2, 8, 3]

x = []
y = []

for k in range(10):
    points_x = randint(1, 15)
    points_y = randint(1, 15)
    x.append(points_x)
    y.append(points_y)

fig = plt.gcf()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(111)

for i in range(len(x)):
    text = ax.text(x[i], y[i], "  b" + str(i), weight="bold")
ax.plot(x, y, c="whitesmoke", linewidth=2, zorder=-10)
ax.scatter(x, y, s=50, c="k", zorder=10)

interp_x = []
interp_y = []

for i in range(0, 1000):
    t = i / 1000
    interp_x.append(De_Casteljau(x, t))
    interp_y.append(De_Casteljau(y, t))

plt.scatter(
    interp_x,
    interp_y,
    s=20,
    c=range(len(interp_x)),
    cmap="viridis",
)

plt.axis("off")
plt.show()
