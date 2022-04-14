import replit
from random import randint, choice

from code.structures import Tree, Mine

class Map:
  def __init__(self,mw,mh,dw,dh,items, game, treeProb, mineProb):
    self.occupiedAreas = []
    self.occupiedList = []
    
    self.mw = mw
    self.mh = mh
    self.dw = dw
    self.dh = dh
    self.pixels = mw * mh

    self.numTrees = int(self.pixels * treeProb)
    self.numMines = int(self.pixels * mineProb)
    
    self.items = items
    self.game = game
    self.pCoords = self.generateCoordinates(1,1)
    
    self.generateMap()
    self.map[self.pCoords[1]][self.pCoords[0]] = '[]'
    self.generateDisplay()
    self.displayWindow()

  def generateMap(self):
    w = self.mw
    h = self.mh

    self.map = []

    default = '  '
    limit = 1000000000
    for i in range(h):
      l = []
      for j in range(w):
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
        l.append(character)
      
      self.map.append(l)

    
    for i in range(self.numTrees):
      self.addTree()

    for i in range(self.numMines):
      self.addMine()
  
  def generateDisplay(self):
    x, y = self.pCoords
    w = self.dw + 2
    h = self.dh + 2
    self.display = self.createFrame(w,h)

    newX = x - ((w-1)//2)
    newY = y - ((h-1)//2)

    if newX < -1:
      newX = -1
    elif newX > self.mw - w + 1:
      newX = self.mw - w + 1

    if newY < -1:
      newY = -1
    elif newY > self.mh - h + 1:
      newY = self.mh - h + 1

    for i in range(h-1):
      for j in range(w-1):
        if i != 0 and i != h - 1 and j != 0 and j != w - 1:
          row = self.map[newY+i]
          character = row[newX+j]
          self.display[i][j] = character
  
  def createFrame(self,w,h):
    frame = []

    top = [['╔'] + ['══' for i in range(w-2)] + ['╗']]
    bottom = [['╚'] + ['══' for i in range(w-2)] + ['╝']]
    
    frame = top + [(['║'] + ['  ' for i in range(w-2)] + ['║']) for j in range(h-2)] + bottom
    
    return frame
    
  def displayWindow(self):
    replit.clear()
    self.generateDisplay()
    window = self.display
    window = [''.join(l) for l in window]
    window = '\n'.join(window)
    print(window)
    print(self.pCoords)
    try:
      self.game.player.printInventory()
    except:
      pass
    

  def setPlayerCoords(self, coords):
    oldx, oldy = self.pCoords

    self.pCoords = coords
    x, y = coords
    if x > self.mw - 1:
      x = self.mw - 1
    elif x < 0:
      x = 0

    if y > self.mh - 1:
      y = self.mh - 1
    elif y < 0:
      y = 0

    if (x,y) not in self.occupiedList:
      self.map[oldy][oldx] = '  '
      character = self.map[y][x]
      if character != '  ':
        self.game.player.addItemToInventory(self.getItem(character))
      self.map[y][x] = '[]'
      if self.pCoords != (oldx,oldy):
        self.displayWindow()
    else:
      self.game.player.coords = (oldx,oldy)
      self.pCoords = (oldx,oldy)
      object = self.findObject(x,y)
      if object.action(self.game.player,self):
        self.deleteStructure(object)
    
    
  def addTree(self):
    tree = Tree()
    treeArr = tree.arr
    treeDims = (len(treeArr[0]),len(treeArr))
    w,h = treeDims
    treeCoords = self.generateCoordinates(w,h)
    

    corners = [treeCoords,(treeCoords[0] + treeDims[0], treeCoords[1] + treeDims[1])]

    x,y = treeCoords
    for i in range(h):
      for j in range(w):
        character = treeArr[i][j]
        self.map[y+i][x+j] = character

    self.addOccupiedArea(corners, tree)

  def addMine(self):
    mine = Mine()
    mineArr = mine.arr
    mineDims = (len(mineArr[0]),len(mineArr))
    w,h = mineDims
    mineCoords = self.generateCoordinates(w,h)

    corners = [mineCoords,(mineCoords[0] + mineDims[0], mineCoords[1] + mineDims[1])]

    x,y = mineCoords
    for i in range(h):
      for j in range(w):
        character = mineArr[i][j]
        self.map[y+i][x+j] = character

    self.addOccupiedArea(corners, mine)
  
  def addOccupiedArea(self, corners, object):
    x1, y1 = corners[0]
    x2, y2 = corners[1]

    object.corners = corners
    
    self.occupiedAreas.append(object)
    

    for i in range(x1,x2):
      for j in range(y1,y2):
        if self.map[j][i] != '  ':
          self.occupiedList.append((i,j))
        
    
  def generateCoordinates(self, w, h):
    x1 = randint(0,self.mw - w)
    x2 = x1 + w
    y1 = randint(0,self.mh - h)
    y2 = y1 + h
    while not self.checkOccupiedAreas(x1,y1,x2,y2):
      x1 = randint(0,self.mw - w)
      x2 = x1 + w
      y1 = randint(0,self.mh - h)
      y2 = y1 + h

    return x1,y1

  def checkOccupiedAreas(self,x1,y1,x2,y2):
    for i in range(x1,x2):
      for j in range(y1,y2):
        if (i,j) in self.occupiedList:
          return False

    return True

  def findObject(self,x,y):
    for object in self.occupiedAreas:
      corners = object.corners
      x1,y1 = corners[0]
      x2,y2 = corners[1]
      if x1 <= x <= x2 and y1 <= y <= y2:
        return object
  def getItem(self,character):
    for item in self.items:
      if character in item.characters:
        return item
  def deleteStructure(self,object):
    corners = object.corners

    x1,y1 = corners[0]
    x2,y2 = corners[1]

    index = self.occupiedAreas.index(object)
    self.occupiedAreas.pop(index)

    print(self.occupiedList)
    
    for i in range(x1,x2):
      for j in range(y1,y2):
        self.map[j][i] = '  '
        if (i,j) in self.occupiedList:
          self.occupiedList.pop(self.occupiedList.index((i,j)))
