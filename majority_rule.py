"""
This module contains an implemetation majority rule cellular automaton.
https://user.eng.umd.edu/~adomaiti/ench250/cachapter.pdf
"""
import sys
import time
import random

from tkinter import Tk, Canvas

GRID_SIZE = 5
SCREEN_SIZE = 1000
NUM_CELLS = SCREEN_SIZE // GRID_SIZE

root = Tk()
canvas = Canvas(root, width=SCREEN_SIZE, height=SCREEN_SIZE)


def draw_automaton(automaton):  
    canvas.delete('all')

    for i in range(NUM_CELLS):
        for j in range(NUM_CELLS):
            if automaton[i][j] == 1:
                x = GRID_SIZE * j
                y = GRID_SIZE * i
                canvas.create_rectangle(
                    x, y, x + GRID_SIZE, y + GRID_SIZE, fill='black'
                )
    
    canvas.update()


def evolve(automaton):
    next_state = [[0 for _ in range(NUM_CELLS)] for _ in range(NUM_CELLS)]

    for i in range(NUM_CELLS):
        for j in range(NUM_CELLS):
            lives = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    lives += automaton[ii % NUM_CELLS][jj % NUM_CELLS]

            if lives >= 5:
                next_state[i][j] = 1
            else:
                next_state[i][j] = automaton[i][j]
    
    return next_state

if __name__ == '__main__':
    generations = 100 if len(sys.argv) < 2 else int(sys.argv[1])
    automaton = [[0 for _ in range(NUM_CELLS)] for _ in range(NUM_CELLS)]
    canvas.delete('all')
    canvas.pack()

    for i in range(NUM_CELLS):
        for j in range(NUM_CELLS):
            automaton[i][j] = 1 if random.random() < 0.33 else 0


    for _ in range(generations):
        time.sleep(0.1)
        automaton = evolve(automaton)
        draw_automaton(automaton)

    root.mainloop()

