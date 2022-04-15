from random import randint
from getkey import getkey, keys
from time import sleep

try:
    from code.map import Map
    from code.player import Player
    from code.util import clearConsole
except:
    from map import Map
    from player import Player
    from util import clearConsole


class Game:
    def __init__(self, mW, mH, dW, dH, items, treeProb, mineProb):
        self.maxWidth = mW
        self.maxHeight = mH
        self.map = Map(mW, mH, dW, dH, items, self, treeProb, mineProb)
        startCoords = self.map.pCoords
        self.player = Player(self, startCoords)
        self.player.setCoords(startCoords[0], startCoords[1])

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

            elif key == '1':
                self.viewInventory()
                self.map.displayWindow()
            elif key == '2':
                self.viewStats()
                self.map.displayWindow()
            elif key == '3':
                self.viewCoordinates()
                self.map.displayWindow()
            elif key == '4':
                self.build()
                self.map.displayWindow()
            elif key == '5':
                self.craft()
                self.map.displayWindow()
            elif key == '6':
                self.clearScreen()
                self.map.displayWindow()

    def getStartCoords(self):
        x = randint(0, self.maxWidth)
        y = randint(0, self.maxHeight)

        return (x, y)

    def viewInventory(self):
        clearConsole()
        self.player.printInventory()
        self.waitForKeypress()

    def viewStats(self):
        clearConsole()
        print('Stats have not been added yet')
        self.waitForKeypress()

    def viewCoordinates(self):
        clearConsole()
        print('Player coordinates: ' + str(self.player.coords))
        self.waitForKeypress()

    def clearScreen(self):
        clearConsole()
        self.map.generateDisplay()
        self.map.displayWindow()

    def build(self):
        clearConsole()
        print('Building has not been added yet')
        self.waitForKeypress()

    def craft(self):
        clearConsole()
        print('Crafting has not been added yet')
        self.waitForKeypress()

    def waitForKeypress(self):
        print('\nPress enter to continue')
        x = input('-> ')
        return
