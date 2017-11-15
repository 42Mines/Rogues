import numpy.random as rd


class Weapon:
    damages = 10
    instability = 1

    def __init__(self, conf):
        self.damages = conf["damages"]
        self.instability = conf["instability"]

    def hit(self, person):
        damages = min(1, rd.normal(self.damages, self.instability))
<<<<<<< HEAD
        person.take_damages(damages)
=======
        return person.takeDamage(damages)
>>>>>>> ec776e0241b4c70bb18c972b3a8b08b830d31dda
