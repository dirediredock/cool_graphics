import matplotlib.pyplot as plt


def recursive_De_Casteljau(points, i, m, t):
    if m == 0:
        return points[i]
    return (
        recursive_De_Casteljau(points, i, m - 1, t) * (1 - t)
        + recursive_De_Casteljau(points, i + 1, m - 1, t) * t
    )


x = [0, 0, 4, 9, 8, 9, 7, 2, 7, 1]
y = [0, 9, 8, 9, 8, 0, 1, 2, 8, 3]

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
    interp_x.append(recursive_De_Casteljau(x, 0, len(x) - 1, t))
    interp_y.append(recursive_De_Casteljau(y, 0, len(y) - 1, t))

plt.scatter(
    interp_x,
    interp_y,
    s=20,
    c=range(len(interp_x)),
    cmap="viridis",
)

plt.axis("off")
plt.show()
