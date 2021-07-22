"""
This module contains an implementation of the model to generate
a Sierpinski triangle.
https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
"""
import sys
import turtle


def sierpinski(side, level, t):
    angle = 60

    if level == 0:
        for _ in range(3):
            t.forward(side)
            t.left(180 - angle)
    else:
        sierpinski(side / 2, level - 1, t)
        t.forward(side / 2)
        sierpinski(side / 2, level - 1, t)
        t.backward(side / 2)
        t.left(angle)
        t.forward(side / 2)
        t.right(angle)
        sierpinski(side / 2, level - 1, t)
        t.left(angle)
        t.backward(side / 2)
        t.right(angle)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ', sys.argv[0], 'generations', 'length')
        exit(0)
    
    generations = int(sys.argv[1])
    length = int(sys.argv[2])

    t = turtle.Turtle()
    t.shape('turtle')

    t.speed(0)
    t.up()
    t.setpos(-length/2, -length/2)
    t.down()
    t.color('black', 'black')
    t.begin_fill()
    sierpinski(length, generations, t)
    t.end_fill()
    turtle.mainloop()

