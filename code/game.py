from random import randint
from getkey import getkey, keys
from time import sleep

from code.map import Map
from code.player import Player

class Game:
  def __init__(self,mW,mH,dW,dH,items,treeProb,mineProb):
    self.maxWidth = mW
    self.maxHeight = mH
    self.map = Map(mW,mH,dW,dH,items,self,treeProb,mineProb)
    startCoords = self.map.pCoords
    self.player = Player(self, startCoords)

  def play(self):
    while True:
      key = getkey()

      if key == 'w' or key == keys.UP:
        self.player.moveUp()
      elif key == 'a' or key == keys.LEFT:
        self.player.moveLeft()
      elif key == 's' or key == keys.DOWN:
        self.player.moveDown()
      elif key == 'd' or key == keys.RIGHT:
        self.player.moveRight()

  
  def getStartCoords(self):
    x = randint(0,self.maxWidth)
    y = randint(0,self.maxHeight)

    return (x,y)