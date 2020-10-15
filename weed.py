"""
This module contains an implementation of a model of weed growing with L-system.
"""
import sys
import turtle
import fractal


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ', sys.argv[0], 'generations', 'length')
        exit(0)
    
    generations = int(sys.argv[1])
    length = int(sys.argv[2])

    t = turtle.Turtle()
    t.speed(0)
    t.shape('turtle')
    t.color('green')

    fractal.set_turtle(t, 0, -250, 90)

    turtle.bgcolor('black')

    production_rules = {
        'F': 'F[RF]F[LF]F'
    }

    weed = fractal.evolve('F', production_rules, generations)

    fractal.draw(t, weed, length, 25, 25)

    turtle.mainloop()
