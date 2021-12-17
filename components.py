import math
import random

import turtle

from status import record_status, recover_status


# plot five star
def five_star(n):
    def _five_star():
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(n / 5)
            turtle.right(144)
            turtle.forward(n / 5)
            turtle.left(72)
        turtle.end_fill()
        turtle.right(126)

    begin_status = record_status()
    turtle.pendown()
    # setting turtle attributions
    turtle.pensize(5)
    turtle.color('orange', 'yellow')
    turtle.left(126)

    _five_star()
    recover_status(begin_status)


# plot leaves of tree
def tree(d, s, pensize=2):
    def _tree(d, s):
        if d <= 0:
            return
        turtle.forward(s)
        _tree(d - 1, s * 0.8)
        turtle.right(120)
        _tree(d - 3, s * 0.5)
        turtle.right(120)
        _tree(d - 3, s * 0.5)
        turtle.right(120)
        turtle.backward(s)

    begin_status = record_status()
    turtle.pendown()
    # set turtle attributions
    turtle.pensize(pensize)
    turtle.color('dark green')
    # plot
    _tree(d, s)
    recover_status(begin_status)


# plot a apple
def apple(size=20):
    def _apple():
        radius_s = size * 2 // 3
        radius_s2 = math.sqrt(2) / 3 * size
        # plot apple's body
        turtle.pensize(size // 10)
        turtle.pencolor('orange')
        turtle.fillcolor('red')
        turtle.begin_fill()

        turtle.setheading(90)
        turtle.circle(size)
        turtle.end_fill()
        turtle.penup()
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size // 3)
        turtle.left(90)
        turtle.circle(-radius_s, 45)
        # plot apple's stride
        turtle.pensize(size // 5)
        turtle.pencolor('brown')

        turtle.left(180)
        turtle.pendown()
        turtle.circle(radius_s, 90)
        turtle.penup()
        turtle.left(180)
        turtle.circle(-radius_s, 45)
        theta = 90 - math.asin(size / 3 / radius_s2) * 360 / (2 * math.pi)
        turtle.right(theta)
        turtle.pendown()
        turtle.circle(-radius_s2, 150)

    begin_status = record_status()
    turtle.pendown()
    _apple()
    recover_status(begin_status)


# plot a flower
def flower(size=10, n=15, pensize=3, color_outline='red', color_fill='yellow'):
    def _flower():
        part_degree = 360 / n
        degree_left = 360 / n
        radius_s = (
            math.sin(part_degree / 2 / 360 * 2 * math.pi) * size
        )  # radius of small circle
        c = 1
        for _ in range(n):
            turtle.circle(c * radius_s, 180)
            turtle.left(degree_left)
            c *= -1
        turtle.end_fill()

    begin_status = record_status()
    turtle.pendown()
    # set turtle attribute
    turtle.pensize(pensize)
    turtle.color(color_outline, color_fill)
    turtle.begin_fill()

    _flower()
    recover_status(begin_status)


# dens 雪花瓣数
def snow(snow_size=10, dens=8, color='white'):
    def _snow():
        for _ in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            turtle.forward(snow_size)
            turtle.backward(snow_size)
            turtle.right(int(360/dens))  # 转动角度

    begin_status = record_status()
    turtle.pendown()
    # setting turtle attributions
    turtle.pensize(1)  # 定义笔头大小
    turtle.pencolor(color)  # 定义画笔颜色为白色，其实就是雪花为白色
    _snow()
    recover_status(begin_status)


def snowing(number=10, random_size: list = [], random_color=False, random_dens: list = False):
    status = record_status()
    w, h = turtle.screensize()
    for _ in range(number):
        x = random.randint(-w, w)
        y = random.randint(-h, h)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        if random_size:
            snow_size = random.randint(random_size[0], random_size[1])
        color = None
        if random_color:
            r = random.randint(0, 255) / 255
            g = random.randint(0, 255) / 255
            b = random.randint(0, 255) / 255
            color = (r, g, b)
        if random_dens:
            dens = random.randint(random_dens[0], random_dens[1])
        snow(snow_size=snow_size if snow_size else 10, dens=dens if dens else 8,
             color=color if color else 'white')
    recover_status(status)
