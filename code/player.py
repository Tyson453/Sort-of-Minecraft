try:
    from code.constants import Constants
    from code.items import Helmet, Chestplate, Leggings, Boots, Axe, Pickaxe
except:
    from constants import Constants
    from items import Helmet, Chestplate, Leggings, Boots, Axe, Pickaxe


class Player:
    def __init__(self, game, startCoords):
        self.inventory = {Constants.DIAMOND_AXE: 1,
                          Constants.DIAMOND_PICKAXE: 2,
                          Constants.STONE_PICKAXE: 1
                          }
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

    def removeItemFromInventory(self, item):
        i = self.inventory[item]
        if i > 1:
            self.inventory[item] -= 1
        elif i == 1:
            self.inventory.pop(item)

    def equipItem(self, item):
        t = type(item)
        if t == Axe:
            self.equipAxe(item)
        elif t == Pickaxe:
            self.equipPickaxe(item)
        elif t == Helmet or t == Chestplate or t == Leggings or t == Boots:
            self.equipArmor(item)

    def equipAxe(self, axe):
        self.removeItemFromInventory(axe)
        if self.axe is not None:
            self.addItemToInventory(self.axe)
        self.axe = axe

    def equipPickaxe(self, pickaxe):
        self.removeItemFromInventory(pickaxe)
        if self.pickaxe is not None:
            self.addItemToInventory(self.pickaxe)
        self.pickaxe = pickaxe

    def equipSword(self, sword):
        self.removeItemFromInventory(sword)
        if self.sword is not None:
            self.addItemToInventory(self.sword)
        self.sword = sword

    def equipArmor(self, armor):
        t = type(armor)

        if t == Helmet:
            self.removeItemFromInventory(armor)
            if self.armor['Helmet'] is not None:
                self.addItemToInventory(self.armor['Helmet'])
            self.armor['Helmet'] = armor
        elif t == Chestplate:
            self.removeItemFromInventory(armor)
            if self.armor['Chestplate'] is not None:
                self.addItemToInventory(self.armor['Chestplate'])
            self.armor['Chestplate'] = armor
        elif t == Leggings:
            self.removeItemFromInventory(armor)
            if self.armor['Leggings'] is not None:
                self.addItemToInventory(self.armor['Leggings'])
            self.armor['Leggings'] = armor
        elif t == Boots:
            self.removeItemFromInventory(armor)
            if self.armor['Boots'] is not None:
                self.addItemToInventory(self.armor['Boots'])
            self.armor['Boots'] = armor

    def printInventory(self):
        print('Sword: ', end='')
        print(self.sword.name if self.sword is not None else None)
        print('Axe: ', end='')
        print(self.axe.name if self.axe is not None else None)
        print('Pickaxe: ', end='')
        print(self.pickaxe.name if self.pickaxe is not None else None)
        print()
        print('Helmet: ', end='')
        print(self.armor['Helmet'].name if self.armor['Helmet']
              is not None else None)
        print('Chestplate: ', end='')
        print(
            self.armor['Chestplate'].name if self.armor['Chestplate'] is not None else None)
        print('Leggings: ', end='')
        print(self.armor['Leggings'].name if self.armor['Leggings']
              is not None else None)
        print('Boots: ', end='')
        print(self.armor['Boots'].name if self.armor['Boots']
              is not None else None)
        print()
        for item in self.inventory:
            print(f'{item.name}: {self.inventory[item]}')
