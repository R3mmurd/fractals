"""
This module contains an example of generating a Koch snowflake.
https://mathworld.wolfram.com/KochSnowflake.html
"""
import sys
import turtle
import fractal


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ', sys.argv[0], 'generations')
        exit(0)
    
    generations = int(sys.argv[1])
    
    start_length = 100

    production_rules = {
        'F': 'FLFRFLF'
    }

    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(0)

    fractal.set_turtle(t, -start_length*3/2, start_length*3/2/2)
    
    curve = fractal.evolve('F', production_rules, generations)

    t.color('blue')

    for _ in range(3):
        fractal.draw(
            t, curve, start_length / (3**(generations-1)),
            left_angle=60, right_angle=120
        )
        t.right(120)

    turtle.mainloop()

