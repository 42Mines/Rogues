import numpy.random as rd


class Weapon:
    damages = 10
    instability = 1

    def __init__(self, conf):
        self.damages = conf["damages"]
        self.instability = conf["instability"]

    def hit(self, person):
        damages = max(1, rd.normal(self.damages, self.instability))
        return person.take_damages(damages)
