import random

import turtle

from components import \
    five_star, tree, flower, apple, bell, snow, fallen_flowers, snowing


def main():
    # global attritutions
    title = 'Christmas tree by Arnaud.'  # 窗口标题
    # 绘画速度(fastest, fast, normal, slow or slowest)
    speed = 'fastest'
    background_color = 'black'          # 背景色
    n = 100                              # 圣诞树尺寸，推荐100

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

    turtle.penup()
    turtle.backward(n / 4)
    turtle.pendown()
    # todo: 画地上的落花
    fallen_flowers(number=200,
                   size=3,
                   wh=(500, 15))

    # todo: 画地上的礼物盒子

    # 下雪
    snowing(number=100,             # 雪花数量
            random_dens=[6, 9],     # 随机瓣数
            random_size=[6, 10],    # 随机雪花尺寸
            random_color=False)     # 随机雪花颜色

    # todo: 写字

    turtle.done()


if __name__ == '__main__':
    main()
