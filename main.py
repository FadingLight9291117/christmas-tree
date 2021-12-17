import turtle

from components import five_star, tree, flower, apple, snowing


def main():
    # global attritutions
    title = 'Christmas tree by Arnaud.'
    speed = 'fastest'  # fastest, fast, normal, slow or slowest
    background_color = 'black'
    n = 80  # 圣诞树尺寸，推荐100

    # set global attri
    turtle.speed(speed)  # set speed
    turtle.title(title)
    turtle.bgcolor(background_color)

    # begin plot
    turtle.left(90)
    turtle.forward(3 * n)

    # plot five star
    five_star(n)

    turtle.penup()
    turtle.backward(n * 4.8)
    turtle.pendown()

    # plot tree rescursively
    tree(15, n, pensize=5)  # 15

    turtle.backward(n / 5)

    # snowing
    snowing(number=30,
                 random_dens=[6, 9],
                 random_size=[6, 10],
                 random_color=False)

    turtle.done()


if __name__ == '__main__':
    main()
