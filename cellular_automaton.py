"""
This module contains the implementation of a cellular automaton
that generates the Serpinski triangle.
https://mathworld.wolfram.com/CellularAutomaton.html
"""


def build_automaton():
    num_cells = 64
    automaton = []

    for _ in range(num_cells):
        automaton.append(0)
    
    # initial condition
    automaton[num_cells//2] = 1

    return automaton


def print_automaton(automaton):
    t = {0: ' ', 1: '*'}
    print(''.join([t[item] for item in automaton]))


def evolve(automaton, num_steps):
    n = len(automaton)

    for _ in range(num_steps):
        next_state = []

        for i in range(n):
            if automaton[(i - 1) % n] == automaton[(i + 1) % n]:
                next_state.append(0)
            else:
                next_state.append(1)
        
        automaton = next_state
        yield automaton



if __name__ == '__main__':
    automaton = build_automaton()
    print_automaton(automaton)
    for state in evolve(automaton, 32):
        print_automaton(state)
