
import curses
from display import *
from Person import Person
from conf import hero_conf
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


hero = Person(5, 5, hero_conf)
caracters = [hero]

while True:
    key = stdscr.getch()

    if key == ord('q'):
        break

    elif curses.KEY_UP:
        hero.setY(hero.getY() + 1)
    elif curses.KEY_DOWN:
        hero.setY(hero.getY() - 1)
    elif curses.KEY_LEFT:
        hero.setX(hero.getX() + 1)
    elif curses.KEY_RIGHT:
        hero.setX(hero.getX() - 1)

    display(stdscr, field, caracters)

# QExitiong curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()


