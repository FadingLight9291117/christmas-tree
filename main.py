import turtle

from components import \
    five_star, tree, flower, apple, snowing, decorate_tree, bell


def main():
    # global attritutions
    title = 'Christmas tree by Arnaud.'     # 窗口标题
    # 绘画速度(fastest, fast, normal, slow or slowest)
    speed = 'fastest'
    background_color = 'white'              # 背景色
    n = 50                                  # 圣诞树尺寸，推荐100

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
    tree(5, n, pensize=5)  # 15

    # turtle.backward(n / 5)
    # todo: 画树上的铃铛
    # todo: 画树上的苹果
    decorate_tree(h=150, degree=0.05, decorators=[bell, apple])

    # turtle.penup()
    # turtle.right(180)
    # turtle.forward(50)
    # turtle.pendown()
    # todo: 画地上的落花
    # todo: 画地上的礼物盒子

    # snowing
    # snowing(number=30,
    #         random_dens=[6, 9],
    #         random_size=[6, 10],
    #         random_color=False)

    # todo: 写字

    turtle.done()


if __name__ == '__main__':
    main()
