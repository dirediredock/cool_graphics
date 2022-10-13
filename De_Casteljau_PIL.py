# by Matias I. Bofarull Oddo - 2022.10.13

from random import randint
from PIL import Image, ImageDraw
from matplotlib.cm import get_cmap


def De_Casteljau(points, t):
    point_array = [point for point in points]
    for i in range(1, len(point_array)):
        for m in range(len(point_array) - i):
            point_array[m] = point_array[m] * (1 - t) + point_array[m + 1] * t
    return point_array[0]


def draw_point(x, y, size, color=(0, 0, 0)):
    draw.ellipse((x - size, y - size, x + size, y + size), color)


num_control_points = 5

WIDTH = 4000
HEIGHT = 4000

image = Image.new("RGB", size=(WIDTH, HEIGHT), color=(255, 255, 255))
draw = ImageDraw.Draw(image)
cmap = get_cmap("viridis")

x = []
y = []

for k in range(num_control_points):
    points_x = randint(int((WIDTH / 20)), WIDTH - int((WIDTH / 20)))
    points_y = randint(int((HEIGHT / 20)), WIDTH - int((HEIGHT / 20)))
    x.append(points_x)
    y.append(points_y)

for i in range(len(x)):
    draw_point(x[i], y[i], size=20)

for i in range(0, 10000):
    t = i / 10000
    Px = int(De_Casteljau(x, t))
    Py = int(De_Casteljau(y, t))
    rgba = cmap(t)
    draw_point(
        Px,
        Py,
        size=15,
        color=(int(rgba[0] * 255), int(rgba[1] * 255), int(rgba[2] * 255)),
    )

draw_point(x[0], y[0], size=25)
draw_point(x[-1], y[-1], size=25)

image.save("De_Casteljau_PIL.png", "PNG")
