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
    turtle.pendown()
