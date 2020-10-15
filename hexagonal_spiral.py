"""
This module contains a fun example of using turtle to draw hexagonal spirals.
"""
import turtle

if __name__ == '__main__':
    colors = ['red', 'blue', 'green', 'yellow', 'pink']
    turtle.bgcolor('black')
    turtle.speed(0)

    for x in range(500):
        turtle.pencolor(colors[x%5])
        turtle.forward(x)
        turtle.left(58)
