from random import randint

def ai(ennemy, hero, terrain):
    abs_x = abs(hero.getX() - ennemy.getX())
    abs_y = abs(hero.getX() - ennemy.getY())
    hero_x = hero.getX()
    hero_y = hero.getY()
    ennemy_x = ennemy.getX()
    ennemy_y = ennemy.getY()

    if abs_X + abs_Y < 8:
        if abs_x == 1 or abs_y == 1:
            ennemy.fight(heros)
        elif hero_x - ennemy_x < 0:
            ennemy.setX(ennemy_x + 1)
        elif hero_x - ennemy_x > 0:
            ennemy.setX(ennemy_x - 1)
        elif hero_y - ennemy_y < 0:
            ennemy.setY(ennemy_y + 1)
        elif hero_y - ennemy_y > 0:
            ennemy.setY(ennemy_y - 1)
    else:
        direction = randint(0, 4)
        if direction == 0:
            ennemy.setY(ennemy_y + 1)
        elif direction == 1:
            ennemy.setY(ennemy_y - 1)
        elif direction == 2:
            ennemy.setX(ennemy_x + 1)
        else:
            ennemy.seyX(ennemy_x - 1)
