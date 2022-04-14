
class Item:
  def __init__(self,name):
    self.name = name


class FloorItem(Item):
  def __init__(self,name,characters,probability):
    self.characters = characters
    self.prob = probability
    Item.__init__(self,name)

class CraftedItem(Item):
  def __init__(self,name,recipe):
    self.recipe = recipe
    Item.__init__(self,name)

class Axe(CraftedItem):
  def __init__(self,name,recipe):
    CraftedItem.__init__(self,name,recipe)

class Pickaxe(CraftedItem):
  def __init__(self,name,recipe):
    CraftedItem.__init__(self,name,recipe)

class Ore:
  def __init__(self,name,prob,req,color):
    characters = ['. ',' .','..','.:',':.','::']
    reset = '\u001b[0m'
    self.characters = [f'{color}{char}{reset}' for char in characters]
    self.req = req
    self.color = color
    self.name = name
    self.prob = prob
