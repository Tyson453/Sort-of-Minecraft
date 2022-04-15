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


class Ore:
    def __init__(self, name, prob, req, color):
        characters = ['. ', ' .', '..', '.:', ':.', '::']
        reset = '\u001b[0m'
        self.characters = [f'{color}{char}{reset}' for char in characters]
        self.req = req
        self.color = color
        self.name = name
        self.prob = prob
