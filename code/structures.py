from random import randint, choice

from code.constants import Constants

class Tree:
  def __init__(self):
    self.generateTree()

  def generateTree(self):
    self.arr = []
    self.arr.append(['  ','__','__','  '])
    self.arr.append([' /','oo','oo','\\ '])
    self.arr.append(['|o','oo','oo','o|'])
    self.arr.append(['|o','oo','oo','o|'])
    self.arr.append([' \\','oo','oo','/ '])
    for i in range(randint(2,4)):
      self.arr.append(['  ','| ',' |','  '])
    self.arr.append(['  ','|_','_|','  '])
      
  def action(self, player, map):
    print()
    if Constants.STONE_AXE not in player.inventory:
      print('You don\'t have an axe so you can\'t chop down the tree')
    else:
      print('What would you like to do?')
      print('1. Chop down the tree')
      print('2. Leave')
      # try:
      x = input('-> ')
      if x == '1':
        self.chop(player)
        return True
      else:
        return False
      # except:
      #   print('Invalid input')
      #   return

  def chop(self,player):
    h = len(self.arr) - 5

    player.addItemToInventory(Constants.ACORN)
    for i in range(h):
      stickChance = randint(1,100) % 2
      leafChance = randint(1,100) % 3
      vineChance = randint(1,100) % 5
      player.addItemToInventory(Constants.LOG)
      if stickChance == 0:
        player.addItemToInventory(Constants.STICK)
      if leafChance == 0:
        player.addItemToInventory(Constants.LEAF)
      if vineChance == 0:
        player.addItemToInventory(Constants.VINE)
    
    

class Mine:
  def __init__(self):
    self.items = Constants.ORES
    self.w = 50
    self.h = 35

  def action(self):
    self.generateMineMap()
  
  def generateMine(self):
    self.arr = []
    self.arr.append([' ╔','══','══','══','╗ '])
    self.arr.append([' ║',' ╔','══','╗ ','║ '])
    self.arr.append([' ║',' ║','  ','║ ','║ '])
    self.arr.append([' ║',' ║','  ','║ ','║ '])
    self.arr.append([' ║',' ║','  ','║ ','║ '])
    self.arr.append(['═╩','═╩','══','╩═','╩═'])
    
    self.generateMineMap()

  def generateMineMap(self):
    w = self.w
    h = self.h

    self.map = self.createFrame(w,h)

    default = '  '
    limit = 1000000000
    for i in range(1,h-1):
      l = []
      for j in range(1,w-1):
        num = randint(1,limit)
        prev = 0
        character = default
        for item in self.items:
          chars = item.characters
          prob = item.prob
          prob += prev
          if num < prob * limit:
            character = choice(chars)
            break

          prev = prob
        self.map[i][j] = character
    

  def display(self):
    window = [''.join(l) for l in self.map]
    window = '\n'.join(window)
    print(window)

  def createFrame(self,w,h):
    frame = []

    top = [['╔'] + ['══' for i in range(w-2)] + ['╗']]
    bottom = [['╚'] + ['══' for i in range(w-2)] + ['╝']]
    
    frame = top + [(['║'] + ['  ' for i in range(w-2)] + ['║']) for j in range(h-2)] + bottom
    
    return frame

'''
Mine
 ╔══════╗ 
 ║ ╔══╗ ║   
 ║ ║  ║ ║ 
 ║ ║  ║ ║ 
 ║ ║  ║ ║ 
═╩═╩══╩═╩═

'''


'''
Tree
    ____
   /oooo\
  |oooooo|
  |oooooo|
   \oooo/
    |  |
    |  | Random amount of trunk from 3-5
    |  |
    |  |
    |  |

'''