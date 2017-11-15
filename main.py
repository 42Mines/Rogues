
import curses
from display import *
from Character import Character
from conf import hero_conf
from map import gen_map

# Initialisation of curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

"""field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]"""

field =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 4, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


hero = Character(3, 3, hero_conf)
characters = [hero]

while True:
    display(stdscr, field, characters)
    key = stdscr.getch()

    if key == ord('q'):
        break

    elif key == curses.KEY_UP and field[hero.get_y() - 1][hero.get_x()] != 0:
        hero.set_y(hero.get_y() - 1)
    elif key == curses.KEY_DOWN and field[hero.get_y() + 1][hero.get_x()] != 0:
        hero.set_y(hero.get_y() + 1)
    elif key == curses.KEY_LEFT and field[hero.get_y()][hero.get_x() - 1] != 0:
        hero.set_x(hero.get_x() - 1)
    elif key == curses.KEY_RIGHT and field[hero.get_y()][hero.get_x() + 1] != 0:
        hero.set_x(hero.get_x() + 1)

    count2 = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if field[hero.get_y() + i][hero.get_x() + j] == 2:
                count2 += 1

    if field[hero.get_y()][hero.get_x()] == 4 and count2 == 0:
        gen_map(hero, field)

    if field[hero.get_y()][hero.get_x()] == 2 and count2 == 1:
        gen_map(hero, field)


    stdscr.addstr(15, 0, "x = {} ; y = {} ; field = {}".format(hero.get_x(), hero.get_y(), field[hero.get_y()][hero.get_x()]))


# QExitiong curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()


