import turtle

from components import fallen_flowers


turtle.speed(0)
turtle.penup()
fallen_flowers(number=200,size=3, wh=(300, 15), colors=['red', 'yellow', 'orange'])

turtle.hideturtle()
turtle.done()