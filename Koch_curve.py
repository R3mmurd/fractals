"""
This module contains an example of generating a simple Koch curve.
https://larryriddle.agnesscott.org/ifs/kcurve/kcurve.htm
"""
import sys
import turtle
import fractal

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ', sys.argv[0], 'generations', 'length')
        exit(0)
    
    generations = int(sys.argv[1])

    start_length = 200

    production_rules = {
        'F': 'FLFRFLF'
    }

    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(0)

    fractal.set_turtle(t, -start_length*3/2, start_length*3/2/2)
    
    curve = fractal.evolve('F', production_rules, generations)

    t.color('red', 'black')
    t.begin_fill()
    
    fractal.draw(t, curve, start_length / (3**(generations-1)), left_angle=60, right_angle=120)

    t.end_fill()

    turtle.mainloop()
