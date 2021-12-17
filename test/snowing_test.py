import turtle

from components import snowing

turtle.speed(0)
# turtle.bgcolor('black')
snowing(number=10,
             random_size=[5, 10],
             random_dens=[6, 9],
             random_color=True)
turtle.done()
