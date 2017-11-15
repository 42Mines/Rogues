import Weapon


class People:
    x = 0
    y = 0

    life = 100
    display = 'P'
    xp_reward = 5
    coins = 0

    weapon = None
    armor = None

    inventory = {weapons: [], armor: []}

    def __init__(self, x, y, conf):
        self.x = x
        self.y = y

        self.xp = 0
        self.xp_reward = conf["xp_reward"]

        self.weapon = Weapon(conf["weapon"])
        inventory["weapons"] = self.weapon

        self.life = conf["life"]

    def fight(self, other):
        self.weapon.hit(other)

    def takeDamages(self, damages):
        if self.armor == None:
            self.life -= damages
        else:
            self.life -= (min(damages - armor.getProtection()), 1)
            armor.use()

            if armor.getLife() <= 0:
                self.armor = None

    def setArmor(self, armor):
        self.armor = armor

    def setWeapon(self, weapon):
        self.weapon = weapon

    def unpack(self, item):
        if item.contains == "weapon":
            self.weapons.push(Weapon(item.config))

        if item.contains == "coin":
            self.coins += item.config["amount"]
