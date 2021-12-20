import random

import turtle

from components import \
    five_star, tree, flower, apple, bell, snow
from status import record_status, recover_status


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


def main():
    # global attritutions
    title = 'Christmas tree by Arnaud.'  # 窗口标题
    # 绘画速度(fastest, fast, normal, slow or slowest)
    speed = 'fastest'
    background_color = 'black'          # 背景色
    n = 80                              # 圣诞树尺寸，推荐100

    # set global attri
    turtle.speed(speed)
    turtle.title(title)
    turtle.bgcolor(background_color)

    # begin plot
    turtle.penup()
    turtle.left(90)
    turtle.forward(3 * n)
    turtle.pendown()

    # plot five star
    five_star(n)

    turtle.penup()
    turtle.backward(n * 4.8)
    turtle.pendown()

    # plot tree rescursively
    tree(d=15,                              # 15
         s=n,
         pensize=4,                         # 树枝尺寸
         decorators=[apple, flower, bell],  # 树上的装饰品
         dense=0.05,                        # 树上装饰品密度
         size=6)                            # 树上装饰品尺寸

    # turtle.backward(n / 5)

    # turtle.penup()
    # turtle.right(180)
    # turtle.forward(50)
    # turtle.pendown()
    # todo: 画地上的落花
    # todo: 画地上的礼物盒子

    # 下雪
    snowing(number=50,              # 雪花数量
            random_dens=[6, 9],     # 随机瓣数
            random_size=[6, 10],    # 随机雪花尺寸
            random_color=False)     # 随机雪花颜色

    # todo: 写字

    turtle.done()


if __name__ == '__main__':
    main()
