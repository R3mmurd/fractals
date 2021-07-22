"""
This module contains an implementeation of Sierpinski arrowhead.
https://mathworld.wolfram.com/SierpinskiArrowheadCurve.html
"""
import sys
import turtle as t
import fractal

def translate(symbol, length, left_angle, right_angle, turtle, turtle_state):
    """
    Translate a symbol into a turtle instruction.
    """
    if symbol == '[':
        turtle_state.append((turtle.xcor(), turtle.ycor(), turtle.heading()))
    elif symbol == ']':
        x, y, h = turtle_state.pop()
        set_turtle(turtle, x, y, h)
    elif symbol == 'F':
        turtle.forward(length)
    elif symbol == '-':
        turtle.left(left_angle)
    elif symbol =='+':
        turtle.right(right_angle)
    elif symbol == 'L':
        turtle.right(right_angle)
        turtle.forward(length)
        turtle.left(left_angle)
        turtle.forward(length)
        turtle.left(left_angle)
        turtle.forward(length)
        turtle.right(right_angle)
    elif symbol == 'R':
        turtle.left(left_angle)
        turtle.forward(length)
        turtle.right(right_angle)
        turtle.forward(length)
        turtle.right(right_angle)
        turtle.forward(length)
        turtle.left(left_angle)

fractal.translate = translate


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ', sys.argv[0], 'generations', 'length')
        exit(0)
    
    generations = int(sys.argv[1])
    length = int(sys.argv[2])

    w = length  * (2 ** (generations + 1))

    turtle = t.Turtle()
    turtle.speed(0)

    t.setup(width=w, height=w, startx=0, starty=0)
    fractal.set_turtle(turtle, -t.window_width() / 2, -t.window_height() / 2)
    t.setup(width=w*1.2, height=w*1.2, startx=0, starty=0)

    production_rules = {
        'L': '+R-L-R+',
        'R': '-L+R+L-'
    }

    arrowhead = fractal.evolve('R', production_rules, generations)

    fractal.draw(turtle, arrowhead, length, 60, 60)

    t.mainloop()

