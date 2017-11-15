from random import randint, random, choice


def link(map, x1, y1, x2, y2):

    assert x1 > x2
    assert y1 > y2

    x, y = x1, y1
    rand_ref = random()

    while x != x2 and y != y2:
        if x == x2:
            y -= 1
            map[y][x] = 2

        elif y == y2:
            x -= 1
            map[y][x] = 2

        else:
            if random() > rand_ref:
                x -= 1
            else:
                y -= 1

            map[y][x] = 2


def gen_map(hero, map):
    density_to_achieve = 0.1  # The percentage we want to fill
    area_to_scan = 30

    # on ajoute des cases en bas à droite pour jouer

    safety = 10
    if len(map[0]) - hero.getX() < safety * area_to_scan:
        for i in range(len(map[0])):
            map[i] = map[i] + [0 for i in safety * area_to_scan]

    if len(map) - hero.getY() < safety * area_to_scan:
        for i in range(safety * area_to_scan):
            map.append([0 for i in range(len(map[0]))])

    # On calcule la densité de salles
    filled = 0
    scanned = 0

    for y in range(-area_to_scan, area_to_scan + 1):
        for x in range(-area_to_scan, area_to_scan + 1):

            if y < 0 or x < 0 or y >= len(map) or x >= len(map[0]):
                continue

            scanned += 1
            if map[y][x] != 0:
                filled += 1

    density = filled / scanned

    if density < density_to_achieve / 3:

        rooms_to_add = randint(1, 4)

        for i in range(rooms_to_add):
            rx = hero.getX()
            ry = hero.getY()

            door_x, door_y = 0, 0  # La distance jusqu'à la sortie de la salle
            while map[ry][rx + door_x] != 0:
                door_x += 1

            while map[ry + door_y][rx] != 0:
                door_y += 1

            #On place la salle et prend ses dimensions
            room_x = rx + door_x + randint(3, 10)
            room_y = ry + door_y + randint(3, 10)

            room_width = randint(5, 12)
            room_height = randint(5, 12)

            #On l'écrit dans le truc
            for x in range(room_width):
                for y in range(room_height):
                    map[room_y + y][room_x + x] = 1

            doors = []

            for y in range(len(map)):
                for x in range(len(map[0])):
                    if map[y][x] == 3:
                        doors.append((x, y))

            #on place des portes

            door_top = False
            if random() > 0.5:
                door_top = True
                door_y = randint(1, room_height) + room_y
                door_x = room_x

                map[door_y][door_x] = 3
                target_x, target_y = choice(doors)
                link(map, door_x, door_y, target_x, target_y)

            if random() > 0.5 or not door_top:
                door_x = randint(1, room_width) + room_x
                door_y = room_y

                map[door_y][door_x] = 3
                link(map, door_x, door_y, target_x, target_y)


            #Note: on devrai générer les nouvelles salles dès qu'on arrive sur un seuil non relié
            door_right = False
            if random() > 0.5:
                door_right = True
                door_y = randint(1, room_height) + room_y
                door_x = room_x + room_width

                map[door_y][door_x] = 3

            if random() > 0.5 or not door_right:
                door_x = randint(1, room_width) + room_x
                door_y = room_y + room_height

                map[door_y][door_x] = 3


