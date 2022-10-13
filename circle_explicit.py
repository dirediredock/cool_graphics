# by Matias I. Bofarull Oddo - 2022.10.05


def circle_half_arc(t):
    return (1 - (t ** 2)) ** (1 / 2)


import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(111)

interp_x = []
interp_pos_y = []
interp_neg_y = []

for i in range(-1000, +1000):
    t = i / 1000
    interp_x.append(t)
    interp_pos_y.append(+circle_half_arc(t))
    interp_neg_y.append(-circle_half_arc(t))

plt.scatter(
    interp_x,
    interp_pos_y,
    s=500,
    c=range(len(interp_x)),
    cmap="viridis",
)
plt.scatter(
    interp_x,
    interp_neg_y,
    s=500,
    c=range(len(interp_x)),
    cmap="inferno",
)

plt.show()
