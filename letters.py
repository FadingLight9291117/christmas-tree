import turtle
import math

from status import record_status, recover_status


def F(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size // 4)
    turtle.pendown()
    turtle.left(90 - angle)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.backward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)

    recover_status(begin_status)


def O(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size // 2)
    turtle.right(angle)
    turtle.pendown()
    turtle.circle(size // 2)

    recover_status(begin_status)


def R(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size // 4)
    turtle.pendown()
    turtle.left(90 - angle)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size // 4)
    turtle.circle(-size // 4, 200)
    turtle.left(180)
    turtle.circle(size // 4, 20)
    turtle.right(50)
    turtle.forward(size // 1.5)

    recover_status(begin_status)


def blank(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size)
    turtle.pendown()

    recover_status(begin_status)


def J(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size // 6)
    turtle.left(90)
    turtle.forward(size // 3)
    turtle.right(90)
    turtle.pendown()

    turtle.right(angle)
    turtle.right(90)
    turtle.circle(size // 3, 180)
    turtle.forward(size * 2 // 3)
    turtle.left(90)
    turtle.forward(size // 3)

    recover_status(begin_status)


def U(size=10, angle=5):
    begin_status = record_status()

    turtle.penup()
    turtle.forward(size // 6)
    turtle.left(90)
    turtle.forward(size // 3)
    turtle.pendown()
    turtle.right(angle)
    turtle.forward(size * 2 // 3)
    turtle.backward(size * 2 // 3)
    turtle.left(180)
    turtle.circle(size // 3, 180)
    turtle.forward(size * 2 // 3)
    turtle.back(size)

    recover_status(begin_status)


def S(size=10, angle=5):
    begin_sta = record_status()

    turtle.pu()
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.backward(size // 4)
    turtle.forward(size // 4)
    turtle.pd()
    turtle.right(angle)
    turtle.left(90)
    turtle.backward(size // 4)
    turtle.forward(size // 4)
    turtle.circle(size // 4, 180)
    turtle.circle(-size // 4, 180)
    turtle.forward(size // 4)

    recover_status(begin_sta)


def T(size=10, angle=5):
    be = record_status()

    turtle.pu()
    turtle.forward(size // 2)
    turtle.pd()
    turtle.right(angle)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size // 3)
    turtle.backward(size * 2 // 3)

    recover_status(be)


def W(size=10, angle=5):
    ang = 30
    be = record_status()

    turtle.pu()
    turtle.forward(size // 2)
    turtle.right(angle)
    turtle.left(90)
    turtle.forward(size)
    turtle.pd()
    ori_p = turtle.position()
    ori_h = turtle.heading()
    turtle.left(180 - ang / 2)
    d = size // math.cos(ang / 2 / 180 * math.pi)
    turtle.forward(d)
    turtle.right(180 - ang)
    turtle.forward(d)
    turtle.pu()
    turtle.setposition(ori_p)
    turtle.setheading(ori_h)
    turtle.pd()
    turtle.right(180 - ang / 2)
    turtle.forward(d)
    turtle.left(180 - ang)
    turtle.forward(d)

    recover_status(be)


def H(size=10, angle=5):
    be = record_status()
    turtle.pu()
    turtle.forward(size // 2)
    turtle.right(angle)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size // 4)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.backward(size)
    turtle.fd(size // 2)
    turtle.right(90)
    turtle.fd(size // 2)
    turtle.left(90)
    turtle.fd(size // 2)
    turtle.backward(size)

    recover_status(be)


def Y(size=10, angle=5):
    be = record_status()

    turtle.pu()
    turtle.forward(size // 2)
    turtle.pd()
    turtle.right(angle)
    turtle.left(90)
    turtle.fd(size // 2)
    turtle.left(30)
    d = size // math.sqrt(3)
    turtle.fd(d)
    turtle.backward(d)
    turtle.right(60)
    turtle.fd(d)

    recover_status(be)


def just_for_why(size=25, pensize=5, color='orange', angle=0):
    turtle.pensize(pensize)
    turtle.pencolor(color)

    string = "Just for why".upper()
    letter2func = {
        ' ': blank,
        'J': J,
        'U': U,
        'S': S,
        'T': T,
        'F': F,
        'O': O,
        'R': R,
        'W': W,
        'H': H,
        'Y': Y,
    }
    for letter in string:
        func = letter2func[letter]
        func(size, angle)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()