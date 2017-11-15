def display(stdscr, field, characters):
    max_x = len(field[0])
    max_y = len(field)

    chars = [" ", ".", "*", "#", "x", "-", "|"]

    for y in range(max_y):
        for x in range(max_x):
            stdscr.addstr(y, x, chars[field[y][x]])

    for character in characters:
        stdscr.addstr(character.get_y(), character.get_x(), character.get_display())
