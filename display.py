from map import gen_map

def display(stdscr, field, characters, fullmode = False):
    height, width = stdscr.getmaxyx()

    offset_x, offset_y = 0, 0
    hero = characters[0]

    while hero.get_x() - offset_x > width / 2 and offset_x < len(field[0]):
        offset_x += int(width / 2)

    while hero.get_y() - offset_y > height / 2 and offset_y < len(field):
        offset_y += int(height / 2)

    max_x = min(len(field[0]), width-5+offset_x)
    max_y = min(len(field), height-5+offset_y)

    field = [field[i][offset_x:max_x] for i in range(offset_y, max_y)]
    stdscr.addstr(height-1, 0, "grid {}x{}".format(len(field), len(field[0])))

    chars = [" ", ".", "*", "#", "x", "-", "|"]

    while len(field) < offset_y + 4 * height:
        field.append([0 for _ in range(len(field[0]))])

    while len(field[0]) < offset_x + 4 * width:
        for line in field:
            for i in range(offset_x + 4 * width):
                line.append(0)

    for y in range(offset_y, max_y):
        for x in range(offset_x, max_x):
            if fullmode:
                stdscr.addstr(y-offset_y, x-offset_x, chars[abs(field[y-offset_y][x-offset_x])])
            else:
                stdscr.addstr(y-offset_y, x-offset_x, chars[max(0, field[y-offset_y][x-offset_x])])

    for character in characters:
        if character == characters[0] or character.dist(characters[0]) < 10:
            stdscr.addstr(character.get_y()-offset_y, character.get_x()-offset_x, character.get_display())
