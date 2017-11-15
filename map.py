from random import randint, random, choice


def link(map, x1, y1, x2, y2):
    assert x1 > x2
    assert y1 > y2

    x, y = x1, y1
    rand_ref = random()

    while x != x2 or y != y2:
        if x == x2:
            y -= 1
            map[y][x] = -2

        elif y == y2:
            x -= 1
            map[y][x] = -2

        else:
            if random() > rand_ref:
                x -= 1
            else:
                y -= 1

            map[y][x] = -2


def gen_map(hero, field):
    density_to_achieve = 0.1  # The percentage we want to fill
    area_to_scan = 10
    safety = 20

    if len(field[0]) - hero.get_x() < safety * area_to_scan:
        for i in range(len(field[0])):
            field[i] = field[i] + [0 for _ in range(safety * area_to_scan)]

    if len(field) - hero.get_y() < safety * area_to_scan:
        for i in range(safety * area_to_scan):
            field.append([0 for _ in range(len(field[0]))])

    filled = 0
    scanned = 0

    for y in range(-area_to_scan, area_to_scan + 1):
        for x in range(-area_to_scan, area_to_scan + 1):

            if y < 0 or x < 0 or y >= len(field) or x >= len(field[0]):
                continue

            scanned += 1
            if field[y][x] != 0:
                filled += 1

    density = filled / scanned

    if density < density_to_achieve / 3:

        rooms_to_add = randint(1, 2)
        #rooms_to_add = 1

        for i in range(rooms_to_add):
            rx = hero.get_x()
            ry = hero.get_y()

            door_x, door_y = 0, 0
            while field[ry][rx + door_x] != 0:
                door_x += 1

            while field[ry + door_y][rx] != 0:
                door_y += 1

            room_x = rx + door_x + randint(3, 10)
            room_y = ry + door_y + randint(3, 10)

            room_width = randint(5, 12)
            room_height = randint(5, 12)

            for x in range(room_width):
                for y in range(room_height):
                    field[room_y + y][room_x + x] = -1

            doors = []

            for y in range(len(field)):
                for x in range(len(field[0])):
                    if field[y][x] == -3:
                        doors.append((x, y))

            target_x, target_y = hero.get_x(), hero.get_y()
            door_top = False
            if random() > 0.5:
                door_top = True
                door_y = randint(1, room_height-1) + room_y
                door_x = room_x

                field[door_y][door_x] = -3
                #target_x, target_y = choice(doors)
                link(field, door_x, door_y, target_x, target_y)

            if random() > 0.5 or not door_top:
                door_x = randint(1, room_width-1) + room_x
                door_y = room_y

                field[door_y][door_x] = -3
                #target_x, target_y = choice(doors)
                link(field, door_x, door_y, target_x, target_y)

            door_right = False
            if random() > 0.5:
                door_right = True
                door_y = randint(1, room_height-1) + room_y
                door_x = room_x + room_width

                field[door_y][door_x] = -3

            if random() > 0.5 or not door_right:
                door_x = randint(1, room_width-1) + room_x
                door_y = room_y + room_height

                field[door_y][door_x] = -3
