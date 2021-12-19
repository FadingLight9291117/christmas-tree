import turtle

from components import decorate_tree, apple, bell


turtle.speed(0)
decorate_tree(n=80, decorators=[apple, bell])

turtle.done()
