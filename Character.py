from Weapon import Weapon


class Character:
    x = 0
    y = 0

    life = 100
    display = 'P'
    xp_reward = 5
    coins = 0

    weapon = None
    armor = None
    inventory = dict()

    inventory = {"weapons": [], "armor": []}

    def __init__(self, x, y, conf):
        self.x = x
        self.y = y

        self.xp = 0
        self.xp_reward = conf["xp_reward"]

        self.weapon = Weapon(conf["weapon"])
        self.inventory["weapons"] = self.weapon

        self.life = conf["life"]

    def fight(self, other):
        return self.weapon.hit(other)

    def take_damages(self, damages):
        mem = self.life
        if self.armor is None:
            self.life -= damages
        else:
            self.life -= (min(damages - self.armor.getProtection()), 1)
            self.armor.use()

            if self.armor.getLife() <= 0:
                self.armor = None

        return mem - self.life

    def set_armor(self, armor):
        self.armor = armor

    def set_weapon(self, weapon):
        self.weapon = weapon

    def unpack(self, item):
        if item.contains == "weapon":
            self.inventory["weapons"].append(Weapon(item.config))

        if item.contains == "coin":
            self.coins += item.config["amount"]

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_display(self):
        return self.display
