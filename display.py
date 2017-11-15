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
#Initialisation of curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

field = [   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,4,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
            [0,0,3,1,1,1,0,2,2,2,2,2,2,2,3,1,1,1,0,0],
            [0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def display(stdscr, field, caracters):
    x = len(field[0])
    y = len(field)
    i = 0;
    j = 0;
    chars = [" ",".","*","#","x","_","|"]


    for i in range(y):
        for j in range(x):
            if field[i][j] == 1:
                if i - 1 > 0 and i + 1 < y and (field[i - 1][j] != 1 or field[i + 1][j] != 1):
                    stdscr.addstr(i, j, chars[5])
                elif i - 1 > 0 and i + 1 < x and (field[i][j - 1] != 1 or field[i][j + 1] != 1):
                    stdscr.addstr(y, x, chars[6])
                else:
                    stdscr.add(i, j, chars[field[y][x]])
            else:
                 strscr.add(i, j, chars[field[y][x]])

display(strscr, field, [])
#QExitiong curses
curses.nocbreak()
stdscr.Keypad(False)
curses.echo()
curses.endwin()
