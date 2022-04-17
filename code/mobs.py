RESET = '\u001b[0m'


class Mob:
    def __init__(self, name, health, damage, loot, color):
        self.name = name
        self.health = health
        self.damage = damage
        self.loot = loot
        self.character = (color + '{}' + RESET)
