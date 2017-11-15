
import curses
from display import *
import Person
#from map import *

# Initialisation of curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


hero = Person()
caracters = [hero]

while True:
    key = stdscr.getch()

    if key == ord('q'):
        break

    display(stdscr, field, [])

# QExitiong curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()


