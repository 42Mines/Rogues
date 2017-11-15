from random import randint

def ai(ennemy, hero, field):

    abs_x = abs(hero.get_x() - ennemy.get_x())
    abs_y = abs(hero.get_x() - ennemy.get_y())
    hero_x = hero.get_x()
    hero_y = hero.get_y()

    ennemy_x = ennemy.get_x()
    ennemy_y = ennemy.get_y()

    dmg = 0
    if abs_x + abs_y < 8:
        if hero_x - ennemy_x > 0 and field[ennemy_y][ennemy_x + 1] != 0:
            ennemy.set_x(ennemy_x + 1)
        elif hero_x - ennemy_x < 0 and field[ennemy_y][ennemy_x + 1] != 0:
            ennemy.set_x(ennemy_x - 1)
        elif hero_y - ennemy_y > 0 and field[ennemy_y + 1][ennemy_x] != 0:
            ennemy.set_y(ennemy_y + 1)
        elif hero_y - ennemy_y < 0 and field[ennemy_y + 1][ennemy_x] != 0:
            ennemy.set_y(ennemy_y - 1)
    else:
        direction = randint(0, 4)
        if direction == 0 and field[ennemy_y + 1][ennemy_x] != 0:
            ennemy.set_y(ennemy_y + 1)
        elif direction == 1 and field[ennemy_y - 1][ennemy_x] != 0:
            ennemy.set_y(ennemy_y - 1)
        elif direction == 2 and field[ennemy_y][ennemy_x + 1] != 0:
            ennemy.set_x(ennemy_x + 1)
        elif field[ennemy_y][ennemy_x - 1] != 0:
           ennemy.set_x(ennemy_x - 1)

    if ennemy.get_x() == hero.get_x() and ennemy.get_y() == hero.get_y():
        ennemy.set_x(ennemy_x)
        ennemy.set_y(ennemy_y)
		   
    return dmg


