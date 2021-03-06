import math
import random

import turtle
from typing_extensions import runtime
from status import record_status, recover_status


# 画五角星
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
    # setting attributions
    turtle.pensize(5)
    turtle.color('orange', 'yellow')
    turtle.left(126)

    _five_star()
    recover_status(begin_status)


# 画苹果
def apple(size=10):
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


# 画花儿
def flower(size=10, n=16, pen_size=3, random_color=True, color='red'):
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
    # set attribute
    turtle.pensize(pen_size)
    if random_color:
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor(r, g, b)
        turtle.fillcolor(r, g, b)
    else:
        turtle.color(color, color)
    turtle.begin_fill()

    _flower()
    recover_status(begin_status)


# 画雪花，dens: 雪花瓣数
def snow(snow_size=10, dens=8, color='white'):
    def _snow():
        for _ in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            turtle.forward(snow_size)
            turtle.backward(snow_size)
            turtle.right(int(360/dens))  # 转动角度

    begin_status = record_status()
    turtle.pendown()
    # setting attributions
    turtle.pensize(1)  # 定义笔头大小
    turtle.pencolor(color)  # 雪花为白色
    _snow()
    recover_status(begin_status)


# 画铃铛
def bell(size=10):
    def _bell():
        turtle.pensize(size / 8)  # 3
        turtle.color("black", '#f8d102')
        turtle.begin_fill()
        turtle.circle(size)  # 25
        turtle.end_fill()

        turtle.penup()
        b_heading = turtle.heading()
        turtle.left(90)
        turtle.forward(size / 3)  # 8
        turtle.setheading(b_heading)
        turtle.pendown()
        turtle.pensize(size / 12)  # 2
        turtle.color("black", '#79675d')
        turtle.begin_fill()
        turtle.circle(size / 5)  # 5
        turtle.end_fill()

        turtle.pensize(size / 8)  # 3
        turtle.right(115)
        turtle.forward(size / 3)  # 7

    begin_status = record_status()
    turtle.pendown()
    _bell()
    recover_status(begin_status)


def gift_box(size=50):
    def _gift_box():
        colors = ['red', 'green', 'blue', 'pink', 'purple', 'brown', 'white']
        rand1 = random.randint(0, len(colors) - 1)
        rand2 = random.randint(0, len(colors) - 1)
        while rand1 == rand2:
            rand2 = random.randint(0, len(colors) - 1)
        color1 = colors[rand1]
        color2 = colors[rand2]
        h = size
        w = size

        # begin plot
        turtle.pencolor('yellow')
        # body
        turtle.fillcolor(color1)
        turtle.begin_fill()
        turtle.left(30)
        turtle.forward(w)
        turtle.right(120)
        turtle.forward(h)
        turtle.right(60)
        turtle.forward(w)
        turtle.right(120)
        turtle.forward(h)
        turtle.left(60)
        turtle.forward(w)
        turtle.left(120)
        turtle.forward(h)
        turtle.left(60)
        turtle.forward(w)
        turtle.left(120)
        turtle.forward(h)
        turtle.end_fill()
        # head
        turtle.fillcolor(color2)
        turtle.begin_fill()
        turtle.left(60)
        turtle.forward(int(w * 1.1))
        turtle.right(60)
        turtle.forward(int(h * 0.2))
        turtle.right(120)
        turtle.forward(int(w * 1.1))
        turtle.right(60)
        turtle.forward(int(h * 0.2))
        turtle.left(120)
        turtle.forward(int(w * 1.1))
        turtle.left(60)
        turtle.forward(int(h * 0.2))
        turtle.left(120)
        turtle.forward(int(w * 1.1))
        turtle.right(60)
        turtle.forward(int(w * 1.1))
        turtle.right(120)
        turtle.forward(int(w * 1.1))
        turtle.right(60)
        turtle.forward(int(w * 1.1))
        turtle.right(120)
        turtle.forward(int(w * 1.1))
        turtle.end_fill()

    begin_status = record_status()
    turtle.pendown()
    _gift_box()
    recover_status(begin_status)


# 画圣诞树, decorators: 圣诞树上的装饰品
def tree(d=15, s=100, pensize=2, decorators: list = None, dense=0.1,  size=5):
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
        # plot decorator
        if decorators is not None and len(decorators) > 0:
            number = random.random()
            if number < dense:
                decorator = decorators[random.randint(0, len(decorators) - 1)]
                decorator(size=size)

    begin_status = record_status()
    turtle.pendown()
    # set attributions
    turtle.pensize(pensize)
    turtle.color('dark green')
    # plot
    _tree(d, s)
    recover_status(begin_status)


# 下雪，随机分布，随机大小的雪花，还可以随机颜色，随机瓣数
def snowing(number=10,
            random_size: list = [5, 10],
            random_color=False,
            random_dens: list = False):
    begin_status = record_status()
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
        snow(snow_size=snow_size if snow_size else 10,
             dens=dens if dens else 8,
             color=color if color else 'white')
    recover_status(begin_status)


def fallen_flowers(number=200, size=3, wh: list = (500, 15), colors=['red', 'yellow', 'orange']):
    begin_status = record_status()
    w, h = wh
    c_x, c_y = turtle.position()
    for _ in range(number):
        x = random.randint(int(-w / 2 + c_x), int(w / 2 + c_x))
        y = random.randint(int(-h / 2 + c_y), int(h / 2 + c_y))
        color = colors[random.randint(0, len(colors)-1)]
        turtle.penup()
        turtle.goto(x, y)
        flower(size=size, random_color=False, color=color)

    recover_status(begin_status)


def snowman(size=100):
    r1 = size // 2
    r2 = int(r1 * 0.6)

    def body():
        be = record_status()

        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.circle(r1, 180)
        turtle.circle(-r2)
        turtle.circle(r1, 180)
        turtle.end_fill()

        # decorate
        turtle.pu()
        turtle.left(90)
        turtle.forward(r1 * 2 // 3)
        turtle.pd()
        turtle.color('black', 'black')
        turtle.begin_fill()
        turtle.circle(r1 // 10)
        turtle.end_fill()
        turtle.pu()
        turtle.forward(r1 * 2 // 3)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(r1 // 10)
        turtle.end_fill()
        turtle.pu()

        # mouth
        turtle.fd(r1 * 2 // 3 + r2 * 2 // 3)
        turtle.pd()
        turtle.right(90)
        turtle.circle(r2 // 4, 90)
        turtle.left(180)
        turtle.circle(-r2 // 4, 180)
        turtle.left(180)
        turtle.circle(r2 // 4, 90)

        # eyes
        turtle.left(90)
        turtle.pu()
        turtle.fd(r2 * 2 // 3)
        turtle.left(90)
        turtle.forward(r2 // 4)
        turtle.pd()
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(r2 // 10)
        turtle.end_fill()
        turtle.pu()
        turtle.backward(r2 * 2 // 5)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(r2 // 10)
        turtle.end_fill()

        recover_status(be)

    def hand():
        be = record_status()

        turtle.pencolor('brown')
        turtle.pensize(r1 // 10)
        turtle.pu()
        turtle.circle(r1, 120)
        turtle.right(90)
        turtle.pd()
        turtle.forward(r1)
        turtle.backward(r1 // 2)
        turtle.left(60)
        turtle.forward(r1 // 2)
        turtle.backward(r1 // 2)
        turtle.right(120)
        turtle.forward(r1 // 2)
        turtle.backward(r1 // 2)
        turtle.left(60)
        turtle.backward(r1 // 2)
        turtle.left(90)

        turtle.pencolor('white')
        turtle.circle(r1, 120)
        turtle.right(90)
        turtle.pencolor('brown')
        turtle.forward(r1)
        turtle.backward(r1 // 2)
        turtle.left(60)
        turtle.forward(r1 // 2)
        turtle.backward(r1 // 2)
        turtle.right(120)
        turtle.forward(r1 // 2)
        turtle.backward(r1 // 2)
        turtle.left(60)
        turtle.backward(r1 // 2)

        recover_status(be)

    def _hat():
        be = record_status()
        turtle.pu()
        turtle.left(90)
        turtle.fd(r1 * 2 + r2 * 2)
        turtle.fd(2)

        turtle.right(90)
        hat(r2)

        recover_status(be)

    be = record_status()
    turtle.pencolor('white')
    turtle.pensize(1)
    body()
    hand()
    _hat()
    recover_status(be)


def hat(size=100, angle=0):
    def _hat():
        r1 = size
        turtle.left(180)
        turtle.begin_fill()
        turtle.circle(r1, 30)
        turtle.right(120)
        turtle.fd(r1 // 5)
        turtle.right(60)
        turtle.circle(-r1, 60)
        turtle.right(60)
        turtle.fd(r1 // 5)
        turtle.right(120)
        turtle.circle(r1, 30)
        turtle.end_fill()

        turtle.circle(r1, 30)
        turtle.right(120)
        turtle.fd(r1 // 5)
        turtle.right(30)
        turtle.color('yellow', 'red')
        turtle.begin_fill()
        turtle.fd(r1)
        turtle.right(120)
        turtle.fd(r1)
        turtle.right(150)
        turtle.circle(r1, 60)
        turtle.end_fill()
        turtle.right(120)
        turtle.right(30)
        turtle.fd(r1)
        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.circle(-r1 // 10)
        turtle.end_fill()

    be = record_status()
    turtle.pd()
    turtle.color('yellow', 'white')
    turtle.right(angle)
    _hat()
    recover_status(be)
