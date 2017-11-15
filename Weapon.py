import numpy.random as rd


class Weapon:
    damages = 10
    instability = 1

    def __init__(self, conf):
        self.damages = conf["damages"]
        self.instability = conf["instability"]

    def hit(self, person):
        damages = min(1, rd.normal(self.damages, self.instability))
        person.takeDamage(damages)
