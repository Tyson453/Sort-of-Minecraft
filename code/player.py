try:
    from code.constants import Constants
except:
    from constants import Constants


class Player:
    def __init__(self, game, startCoords):
        self.inventory = {}
        self.game = game
        x, y = startCoords
        self.coords = startCoords
        self.axe = None
        self.pickaxe = None
        self.sword = None
        self.armor = {'Helmet': None, 'Chestplate': None,
                      'Leggings': None, 'Boots': None}

    def setCoords(self, x, y):
        self.coords = (x, y)
        self.game.map.setPlayerCoords(self.coords)

    def moveLeft(self):
        x, y = self.coords
        x -= 1
        x, y = self.checkCoords(x, y)
        self.setCoords(x, y)

    def moveUp(self):
        x, y = self.coords
        y -= 1
        x, y = self.checkCoords(x, y)
        self.setCoords(x, y)

    def moveRight(self):
        x, y = self.coords
        x += 1
        x, y = self.checkCoords(x, y)
        self.setCoords(x, y)

    def moveDown(self):
        x, y = self.coords
        y += 1
        x, y = self.checkCoords(x, y)
        self.setCoords(x, y)

    def checkCoords(self, x, y):
        if x > self.game.map.mw - 1:
            x = self.game.map.mw - 1
        elif x < 0:
            x = 0

        if y > self.game.map.mh - 1:
            y = self.game.map.mh - 1
        elif y < 0:
            y = 0

        return x, y

    def addItemToInventory(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def printInventory(self):
        for item in self.inventory:
            print(f'{item.name}: {self.inventory[item]}')
