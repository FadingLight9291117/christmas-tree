import math
import random

import turtle
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
            rand2 = random.randint(0, len(colors))
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
        turtle.aright(60)
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
        turtle.forwardint(h * 0.2)
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
