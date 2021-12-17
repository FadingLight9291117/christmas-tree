import turtle


# record turtle beginning status
def record_status():
    begin_pensize = turtle.pensize()
    begin_color = turtle.color()
    begin_positon = turtle.position()
    begin_heading = turtle.heading()

    return [begin_pensize, begin_color, begin_positon, begin_heading]


# recover turtle beginning status
def recover_status(status):
    begin_pensize, begin_color, begin_positon, begin_heading = status
    turtle.pensize(begin_pensize)
    turtle.color(*begin_color)
    turtle.penup()
    turtle.setposition(begin_positon)
    turtle.setheading(begin_heading)


# plot five star
def five_star(n):
    begin_status = record_status()
    turtle.pendown()

    # setting turtle attributions
    turtle.pensize(5)
    turtle.color('orange', 'yellow')
    turtle.left(126)

    def _five_star():
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(n / 5)
            turtle.right(144)
            turtle.forward(n / 5)
            turtle.left(72)
        turtle.end_fill()
        turtle.right(126)

    _five_star()
    recover_status(begin_status)


# plot leaves of tree
def tree(d, s):
    begin_status = record_status()
    turtle.pendown()

    # set turtle attributions
    turtle.pensize(5)
    turtle.color('dark green')

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

    _tree(d, s)
    recover_status(begin_status)


# plot a apple
def apple(size=None, color='red'):
    turtle.pensize(1)
    turtle.color('red', 'red')
    # turtle.circle(100, 180, 10)


# plot a flower
def flower(size=10, n=15, pensize=3, color_outline='red', color_fill='yellow'):
    import math

    begin_status = record_status()
    turtle.pendown()

    # set turtle attribute
    turtle.pensize(pensize)
    turtle.color(color_outline, color_fill)
    turtle.begin_fill()

    def _flower():
        part_degree = 360 / n
        degree_left = 360 / n
        radius_s = (
            math.sin(part_degree / 2 / 360 * 2 * math.pi) * size
        )  # radius of small circle
        c = 1
        for i in range(n):
            turtle.circle(c * radius_s, 180)
            turtle.left(degree_left)
            c *= -1
        turtle.end_fill()

    _flower()
    recover_status(begin_status)


# dens 雪花瓣数
def snow(snow_size=10, dens=10, color_outline='black'):
    begin_status = record_status()
    turtle.pendown()

    # setting turtle attributions
    turtle.pensize(2)  # 定义笔头大小
    turtle.pencolor(color_outline)  # 定义画笔颜色为白色，其实就是雪花为白色

    def _snow():
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            turtle.fd(snow_size)
            turtle.backward(snow_size)
            turtle.right(int(360/dens))  # 转动角度
    _snow()

    recover_status(begin_status)


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


def test():
    snow()
    turtle.done()


if __name__ == '__main__':
    test()
    # main()
