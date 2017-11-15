# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jfarinha <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/15 12:08:24 by jfarinha          #+#    #+#              #
#    Updated: 2017/11/15 13:33:19 by jfarinha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import curses

# Initialisation of curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 3, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 0, 0],
         [0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def display(stdscr, field, caracters):
    max_x = len(field[0])
    max_y = len(field)

    chars = [" ", ".", "*", "#", "x", "_", "|"]

    for y in range(max_y):
        for x in range(max_x):
            if field[y][x] == 1:
                if y - 1 > 0 and y + 1 < y and (field[y - 1][x] != 1 or field[y + 1][x] != 1):
                    stdscr.addstr(y, x, chars[5])
                elif x - 1 > 0 and x + 1 < x and (field[y][x - 1] != 1 or field[y][x + 1] != 1):
                    stdscr.addstr(y, x, chars[6])
                else:
                    stdscr.addstr(y, x, chars[field[y][x]])
            else:
                stdscr.addstr(y, x, chars[field[y][x]])


display(stdscr, field, [])


while True:
    key = stdscr.getch()
    print(key)
    if key == ord('a'):
        break

# QExitiong curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

