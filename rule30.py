"""
This module contains an implementation of the rule 30.
https://en.wikipedia.org/wiki/Rule_30
"""
def build_automaton(num_cells):
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
    rules = {
        '111': 0, '110': 0, '101': 0, '000': 0,
        '100': 1, '011': 1, '010': 1, '001': 1
    }

    state = [0] + automaton + [0]

    n = len(automaton)

    for _ in range(num_steps):
        next_state = []

        for i in range(1, n + 1):
            pattern = f'{state[i - 1]}{state[i]}{state[i + 1]}'
            next_state.append(rules[pattern])
        
        state = [0] + next_state + [0]
        yield state[1:-1]



if __name__ == '__main__':
    automaton = build_automaton(100)
    print_automaton(automaton)
    for state in evolve(automaton, 50):
        print_automaton(state)
