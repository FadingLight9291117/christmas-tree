import turtle

from components import random_snows

turtle.speed(0)
# turtle.bgcolor('black')
random_snows(number=10,
             random_size=[5, 10],
             random_dens=[6, 9],
             random_color=True)
turtle.done()
