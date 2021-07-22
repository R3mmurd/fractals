"""
This module contains an example of generating a simple dragon curve.
https://en.wikipedia.org/wiki/Dragon_curve
"""
import sys
import turtle
import fractal

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python', sys.argv[0], 'generations')
        exit(0)
    
    generations = int(sys.argv[1])
    start_length = 100

    production_rules = {
        'F': 'FLFRFRFFLFLFRF'
    }

    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(0)
    
    fractal.set_turtle(t, -start_length*3/2, 0)

    curve = fractal.evolve('F', production_rules, generations)

    t.color('red', 'black')
    t.begin_fill()
    
    fractal.draw(
        t, curve, start_length / (4**(generations-1)),
        left_angle=90, right_angle=90
    )

    t.end_fill()
    turtle.mainloop()

