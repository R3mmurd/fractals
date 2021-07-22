"""
This module contains an example of generating a Jurassic Park dragon.
https://en.wikipedia.org/wiki/Dragon_curve#Heighway_dragon
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
    
    production_rules = {
        'X': 'XRYFR',
        'Y': 'LFXLY'
    }

    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(0)
    
    fractal.set_turtle(t, -length*3/2, 0)
    
    curve = fractal.evolve('FX', production_rules, generations)

    t.color('red')
    
    fractal.draw(t, curve, length, left_angle=90, right_angle=90)

    turtle.mainloop()

