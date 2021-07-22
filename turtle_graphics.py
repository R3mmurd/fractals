"""
This modue contains a fun example of using turtle to draw circles.
"""
import turtle

if __name__ == '__main__':
    turtle.screensize(1000, 1000)
    turtle.pensize(6)

    for i in range(10):
        turtle.color((1, i/10, 0))
        turtle.circle(100)
        turtle.right(360/10)

