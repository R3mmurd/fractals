"""
This module contains the implementation of functions to generate fratals.

https://es.wikipedia.org/wiki/Fractal
"""
def set_turtle(turtle, x, y, h=0):
    turtle.up()
    turtle.setx(x)
    turtle.sety(y)
    turtle.setheading(h)
    turtle.down()


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
    elif symbol == 'L':
        turtle.left(left_angle)
    elif symbol =='R':
        turtle.right(right_angle)



def evolve(axiom, production_rules, generations):
    """
    Evolve the fractal production by a number of generations 
    """
    state = axiom

    for _ in range(generations):
        next_state = ''

        for s in state:
            if s in production_rules:
                next_state += production_rules[s]
            else:
                next_state += s

        state = next_state

    return state


def draw(turtle, curve, length, left_angle, right_angle):
    """
    Draw a curve.
    """
    turtle_state = []
    for c in curve:
        translate(c, length, left_angle, right_angle, turtle, turtle_state)

