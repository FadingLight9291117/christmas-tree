import turtle

from components import five_star, tree, flower, apple, snow


def main():
    title = 'Christmas tree by Arnaud.'
    speed = 'fastest'  # fastest, fast, normal, slow or slowest
    n = 50  # 100

    turtle.speed(speed)  # set speed
    turtle.title(title)

    turtle.left(90)
    turtle.forward(3 * n)

    # plot five star
    five_star(n)

    turtle.penup()
    turtle.backward(n * 4.8)
    turtle.pendown()

    # plot tree rescursively
    tree(15,  n)  # 15

    turtle.backward(n / 5)
    turtle.pensize(1)

    turtle.done()



if __name__ == '__main__':
    main()
