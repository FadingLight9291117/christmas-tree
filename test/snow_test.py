import random

import turtle

from components import snow

turtle.speed(0)
turtle.bgcolor('black')
h, w = turtle.screensize()
for _ in range(10):
    x = random.randint(-w, w)
    y = random.randint(-h, h)
    turtle.goto(x, y)
    snow_size = random.randint(5, 10)
    snow(snow_size=snow_size)

turtle.done()
