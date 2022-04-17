from code.items import Item, FloorItem, CraftedItem, Sword, Axe, Pickaxe, Ore


class Constants:
    # <Colors>
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'  # Ruby
    GREEN = '\u001b[32m'  # Jade
    YELLOW = '\u001b[33m'  # Gold
    ORANGE = '\u001b[34m'  # Copper
    MAGENTA = '\u001b[35m'  # Amethyst
    CYAN = '\u001b[36m'  # Diamond
    WHITE = '\u001b[37m'  # Silver
    RESET = '\u001b[0m'
    # </Colors>

    # <Characters>
    PLAYER = '[]'
    # </Characters>

    # <Items>
    # <Floor>
    STICK = FloorItem('Stick', ['══'], .002)
    ROCK = FloorItem('Rock', ['o ', ' o'], .001)
    LEAF = FloorItem('Leaf', ['{>', '<}'], .0009)
    VINE = FloorItem('Vine', [') ', '( ', ' )', ' ('], .00075)

    # <Ore>
    COPPER = Ore('Copper ore', .0025, 1, ORANGE)
    SILVER = Ore('Silver ore', .001, 2, WHITE)
    GOLD = Ore('Gold ore', .00075, 2, YELLOW)
    AMETHYST = Ore('Amethyst', .0004, 3, MAGENTA)
    JADE = Ore('Jade', .0002, 3, GREEN)
    RUBY = Ore('Ruby', .00015, 4, RED)
    DIAMOND = Ore('Diamond', .0001, 5, CYAN)

    ORES = [COPPER, SILVER, GOLD, AMETHYST, JADE, RUBY, DIAMOND]
    # </Ore>
    # </Floor>

    # <Obtained>
    LOG = Item('Log')
    ACORN = Item('Acorn')
    # </Obtained>

    # <Crafted>
    # <Tools>
    # <Stone>
    STONE_SWORD = Sword(75, 'Stone sword', None, 15)
    STONE_AXE = Axe(75, 'Stone axe', {STICK: 2, ROCK: 3, VINE: 1})
    STONE_PICKAXE = Pickaxe(75, 'Stone pickaxe', {
                            STICK: 2, ROCK: 3, VINE: 2}, 1)
    # </Stone>
    # <Copper>
    COPPER_SWORD = Sword(150, 'Copper sword', None, 25)
    COPPER_AXE = Axe(150, 'Copper axe', None)
    COPPER_PICKAXE = Pickaxe(150, 'Copper pickaxe', None, 2)
    # </Copper>
    # <Silver>
    SILVER_SWORD = Sword(250, 'Silver sword', None, 35)
    SILVER_AXE = Axe(250, 'Silver axe', None)
    SILVER_PICKAXE = Pickaxe(250, 'Silver pickaxe', None, 3)
    # </Silver>
    # <Jade>
    JADE_SWORD = Sword(400, 'Jade sword', None, 45)
    JADE_AXE = Axe(400, 'Jade axe', None)
    JADE_PICKAXE = Pickaxe(400, 'Jade pickaxe', None, 4)
    # </Jade>
    # <Ruby>
    RUBY_SWORD = Sword(550, 'Ruby sword', None, 45)
    RUBY_AXE = Axe(550, 'Ruby axe', None)
    RUBY_PICKAXE = Pickaxe(550, 'Ruby pickaxe', None, 5)
    # </Ruby>
    # <Diamond>
    DIAMOND_SWORD = Sword(750, 'Diamond sword', None, 55)
    DIAMOND_AXE = Axe(750, 'Diamond axe', None)
    DIAMOND_PICKAXE = Pickaxe(750, 'Diamond pickaxe', None, 6)
    # </Diamond>
    # </Tools>

    # <Armor>

    # <Armor>
    # </Crafted>

    # </Items>
