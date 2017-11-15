import weapon

class Item:

	x = 0
	y = 0
	contains = ""
	config = {}

	def __init__(self, x, y, contains, config):
		self.x = x
		self.y = y
		self.contains = contains
		self.config = config

	