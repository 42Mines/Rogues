import curses
from display import *
from ai import *
from Character import Character
from conf import hero_conf, ennemies_conf
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

<<<<<<< HEAD
field =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

=======
field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 3, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
>>>>>>> ec776e0241b4c70bb18c972b3a8b08b830d31dda

hero = Character(3, 3, hero_conf)
snake = Character(1, 1, ennemies_conf["snake"])
characters = [hero, snake]
ennemies = [snake]

fullmode = False

while True:
    display(stdscr, field, characters, fullmode)
    key = stdscr.getch()

    if key == ord('q'):
        break

    elif key == ord('f'):
        if fullmode:
            fullmode = False
        else:
            fullmode = True

    elif key == curses.KEY_UP and field[hero.get_y() - 1][hero.get_x()] != 0:
        hero.set_y(hero.get_y() - 1)
    elif key == curses.KEY_DOWN and field[hero.get_y() + 1][hero.get_x()] != 0:
        hero.set_y(hero.get_y() + 1)
    elif key == curses.KEY_LEFT and field[hero.get_y()][hero.get_x() - 1] != 0:
        hero.set_x(hero.get_x() - 1)
    elif key == curses.KEY_RIGHT and field[hero.get_y()][hero.get_x() + 1] != 0:
        hero.set_x(hero.get_x() + 1)

    if field[hero.get_y()][hero.get_x()] == -1:
        y, x = hero.get_y(), hero.get_x()
        min_x, min_y = x, y
        max_x, max_y = x, y

        while field[y][min_x] == -1:
            min_x -= 1

        while field[y][max_x] == -1:
            max_x += 1

        while field[min_y][x] == -1:
            min_y -= 1

        while field[max_y][x] == -1:
            max_y += 1

        for i in range(min_y, max_y + 1):
            for j in range(min_x, max_x + 1):
                field[i][j] = abs(field[i][j])

    field[hero.get_y()][hero.get_x()] = abs(field[hero.get_y()][hero.get_x()])

    count2 = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(field[hero.get_y() + i][hero.get_x() + j]) == 2:
                count2 += 1

    if field[hero.get_y()][hero.get_x()] == 3 and count2 == 0:
        gen_map(hero, field)
        stdscr.addstr(30, 0, "{}".format(count2))

    if field[hero.get_y()][hero.get_x()] == 2 and count2 == 1:
        gen_map(hero, field)
<<<<<<< HEAD

    for ennemy in ennemies:
        dmg = ai(ennemy, hero, field)
       # if (dmg != 0):
        stdscr.addstr(31, 0, "{} did {} damage to player".format(snake.get_type, dmg))
    
    stdscr.addstr(15, 0, "x = {} ; y = {} ; field = {}".format(hero.get_x(), hero.get_y(), field[hero.get_y()][hero.get_x()]))
=======
        stdscr.addstr(32, 0, "{}".format(count2))
>>>>>>> ec776e0241b4c70bb18c972b3a8b08b830d31dda

# QExitiong curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
