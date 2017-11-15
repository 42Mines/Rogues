import np.random.normal as normal

class Weapon:

	damages = 10
	instability = 1

	def __init__(self, conf):
		self.damages = conf["damages"]
		self.instability = conf["instability"]

	def hit(self, person):
		damages = min(1, normal(damages, instability))
		person.takeDamage(damages)
