"""
This module contains an implementation of the Lindenmayer's system (L-system)
for modeling the growth of algae.
https://en.wikipedia.org/wiki/L-system

"""
import sys

prodution_rules = {
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E',
    'E': 'F',
    'F': 'AB'
}


def evolve(l):
    return prodution_rules[l]


def iterate(n):
    Lsystem = 'A'

    for _ in range(n):
        print(Lsystem)
        tmp = ''

        for c in Lsystem:
            tmp += evolve(c)
        
        Lsystem = tmp

    print('Number of algae:', len(Lsystem))


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 10
    iterate(n)
  