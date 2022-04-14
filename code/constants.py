from code.items import Item,FloorItem,CraftedItem,Axe,Pickaxe,Ore

class Constants:
  # <Colors>
  BLACK = '\u001b[30m' # Coal
  RED = '\u001b[31m' # Copper
  GREEN = '\u001b[32m' # Jade
  YELLOW = '\u001b[33m' # Gold
  BLUE = '\u001b[34m' # Diamond
  MAGENTA = '\u001b[35m' # Amethyst
  CYAN = '\u001b[36m'
  WHITE = '\u001b[37m' # Titanium
  RESET = '\u001b[0m'
  # </Colors>
  
  # <Characters>
  PLAYER = '[]'
  # </Characters>

  # <Items>

  # <Floor>
  STICK = FloorItem('Stick',['══'],.002)
  ROCK = FloorItem('Rock',['o ',' o'],.001)
  LEAF = FloorItem('Leaf',['{>','<}'],.0009)
  VINE = FloorItem('Vine',[') ','( ',' )',' ('],.00075)

  # <Ore>
  COPPER = Ore('Copper ore',.005,None,RED)
  SILVER = Ore('Silver ore',.002,None,WHITE)
  GOLD = Ore('Gold ore',.001,None,YELLOW)
  AMETHYST = Ore('Amethyst',.00075,None,MAGENTA)
  JADE = Ore('Jade',.0005,None,GREEN)
  DIAMOND = Ore('Diamond',.0002,None,BLUE)

  ORES = [COPPER,SILVER,GOLD,AMETHYST,JADE,DIAMOND]
  
  # </Ore>
  # </Floor>

  # <Crafted>
  # <Tools>
  # <Stone>
  STONE_AXE = Axe('Stone axe',None)
  STONE_PICKAXE = Pickaxe('Stone pickaxe',None)
  # </Stone>
  # </Tools>
  # </Crafted>

  # <Obtained>
  LOG = Item('Log')
  ACORN = Item('Acorn')
  # </Obtained>
  # </Items>
  