class Item:
    def __init__(self, name):
        self.name = name


class FloorItem(Item):
    def __init__(self, name, characters, probability):
        self.characters = characters
        self.prob = probability
        Item.__init__(self, name)


class CraftedItem(Item):
    def __init__(self, name, recipe):
        self.recipe = recipe
        Item.__init__(self, name)


class Tool(CraftedItem):
    def __init__(self, durability, name, recipe):
        self.durability = durability
        CraftedItem.__init__(self, name, recipe)


class Axe(Tool):
    def __init__(self, durability, name, recipe):
        Tool.__init__(self, durability, name, recipe)


class Pickaxe(Tool):
    def __init__(self, durability, name, recipe, power):
        self.power = power
        Tool.__init__(self, durability, name, recipe)


class Sword(Tool):
    def __init__(self, durability, name, recipe, damage):
        self.damage = damage
        Tool.__init__(self, durability, name, recipe)


class Armor(CraftedItem):
    def __init__(self, name, recipe, durability, defense):
        CraftedItem.__init__(self, name, recipe)
        self.durability = durability
        self.defense = defense


class Helmet(Armor):
    def __init__(self, name, recipe, durability, defense):
        Armor.__init__(self, name, recipe, durability, defense)


class Chestplate(Armor):
    def __init__(self, name, recipe, durability, defense):
        Armor.__init__(self, name, recipe, durability, defense)


class Leggings(Armor):
    def __init__(self, name, recipe, durability, defense):
        Armor.__init__(self, name, recipe, durability, defense)


class Boots(Armor):
    def __init__(self, name, recipe, durability, defense):
        Armor.__init__(self, name, recipe, durability, defense)

class Ore:
    def __init__(self, name, prob, req, color):
        characters = ['. ', ' .', '..', '.:', ':.', '::']
        reset = '\u001b[0m'
        self.characters = [f'{color}{char}{reset}' for char in characters]
        self.req = req
        self.color = color
        self.name = name
        self.prob = prob
