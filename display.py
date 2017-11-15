def display(stdscr, field, characters, fullmode = False):
    height, width = stdscr.getmaxyx()

    max_x = min(len(field[0]), width-5)
    max_y = min(len(field), height-5)

    field = [field[i][0:max_x] for i in range(max_y)]
    stdscr.addstr(height-1, 0, "grid {}x{}".format(len(field), len(field[0])))

    chars = [" ", ".", "*", "#", "x", "-", "|"]

    for y in range(max_y):
        for x in range(max_x):
            if fullmode:
                stdscr.addstr(y, x, chars[abs(field[y][x])])
            else:
                stdscr.addstr(y, x, chars[max(0, field[y][x])])

    for character in characters:
        stdscr.addstr(character.get_y(), character.get_x(), character.get_display())
