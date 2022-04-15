try:
    from code.items import Item, FloorItem, CraftedItem, Axe, Pickaxe, Ore
except:
    from items import Item, FloorItem, CraftedItem, Axe, Pickaxe, Ore


class Constants:
    # <Colors>
    BLACK = '\u001b[30m'  # Coal
    RED = '\u001b[31m'  # Copper
    GREEN = '\u001b[32m'  # Jade
    YELLOW = '\u001b[33m'  # Gold
    BLUE = '\u001b[34m'  # Diamond
    MAGENTA = '\u001b[35m'  # Amethyst
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'  # Titanium
    RESET = '\u001b[0m'
    # </Colors>

    # <Characters>
    PLAYER = '[]'
    # </Characters>

    # <Items>
    # <Crafted>
    # <Tools>
    # <Stone>
    STONE_AXE = Axe('Stone axe', None)
    STONE_PICKAXE = Pickaxe('Stone pickaxe', None)
    # </Stone>
    # <Copper>
    COPPER_AXE = Axe('Copper axe', None)
    COPPER_PICKAXE = Pickaxe('Copper pickaxe',None)
    # </Copper>
    # <Silver>
    SILVER_AXE = Axe('Silver axe', None)
    SILVER_PICKAXE = Pickaxe('Silver pickaxe', None)
    # </Silver>
    # <Gold>
    GOLD_AXE = Axe('Gold axe', None)
    GOLD_PICKAXE = Pickaxe('Gold pickaxe', None)
    # </Gold>
    
    # <Jade>
    JADE_AXE = Axe('Jade axe', None)
    JADE_PICKAXE = Pickaxe('Jade pickaxe', None)
    # </Jade>
    # <Diamond>
    DIAMOND_AXE = Axe('Diamond axe', None)
    DIAMOND_PICKAXE = Pickaxe('Diamond pickaxe', None)
    
    # </Diamond>
    
    
    # </Tools>
    # </Crafted>

    # <Floor>
    STICK = FloorItem('Stick', ['══'], .002)
    ROCK = FloorItem('Rock', ['o ', ' o'], .001)
    LEAF = FloorItem('Leaf', ['{>', '<}'], .0009)
    VINE = FloorItem('Vine', [') ', '( ', ' )', ' ('], .00075)

    # <Ore>
    COPPER = Ore('Copper ore', .005, STONE_PICKAXE, RED)
    SILVER = Ore('Silver ore', .002, COPPER_PICKAXE, WHITE)
    GOLD = Ore('Gold ore', .001, SILVER_PICKAXE, YELLOW)
    AMETHYST = Ore('Amethyst', .00075, SILVER_PICKAXE, MAGENTA)
    JADE = Ore('Jade', .0005, GOLD_PICKAXE, GREEN)
    DIAMOND = Ore('Diamond', .0002, JADE_PICKAXE, BLUE)

    ORES = [COPPER, SILVER, GOLD, AMETHYST, JADE, DIAMOND]

    # </Ore>
    # </Floor>

    # <Obtained>
    LOG = Item('Log')
    ACORN = Item('Acorn')
    # </Obtained>
    # </Items>
