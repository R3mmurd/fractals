"""
This module contains an example of the implementation of the Cantor Set.
https://en.wikipedia.org/wiki/Cantor_set
"""
from tkinter import Tk, Canvas


def cantor_set(x, y, l, win):
    if l <= 1:
        # Stop recursion calls when the line is 1 pixel or fewer.
        return
    
    win.create_line(x, y, x + l, y)

    # Draw the next set 50 pixels below.
    y += 50

    cantor_set(x, y, l/3, win)
    cantor_set(x + 2/3 * l, y, l/3, win)


if __name__ == '__main__':
    w, h = 1800, 350
    root = Tk()
    win = Canvas(root, width=w, height=h)
    win.master.title('Cantor Set')
    win.pack()
    cantor_set(10, 10, w-20, win)
    root.mainloop()

