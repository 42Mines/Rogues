def display(stdscr, field, caracters):
    max_x = len(field[0])
    max_y = len(field)

    chars = [" ", ".", "*", "#", "x", "-", "|"]

    for y in range(max_y):
        for x in range(max_x):
            if field[y][x] == 1:
                if y - 1 > 0 and y + 1 < max_y:
                    if field[y - 1][x] == 0:
                        stdscr.addstr(y - 1, x, chars[5])
                    if field[y + 1][x] == 0:
                        stdscr.addstr(y + 1, x, chars[5])
                if x - 1 > 0 and x + 1 <max_x:
                    if field[y][x - 1] == 0:
                        stdscr.addstr(y, x - 1, chars[6])
                    if field[y][x + 1] == 0:
                        stdscr.addstr(y, x + 1, chars[6])
                else:
                    stdscr.addstr(y, x, chars[field[y][x]])
            elif field[y][x] != 0:
                stdscr.addstr(y, x, chars[field[y][x]])

	for character in characters:
        stdscr.addstr(character.get_y(), character.get_x(), character.get_display())