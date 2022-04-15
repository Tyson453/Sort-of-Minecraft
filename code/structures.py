from random import randint, choice
from getkey import getkey, keys


try:
    from code.constants import Constants
    from code.util import clearConsole
except:
    from constants import Constants
    from util import clearConsole


class Tree:
    def __init__(self):
        self.generateTree()

    def generateTree(self):
        self.arr = []
        self.arr.append(['  ', '__', '__', '  '])
        self.arr.append([' /', 'oo', 'oo', '\\ '])
        self.arr.append(['|o', 'oo', 'oo', 'o|'])
        self.arr.append(['|o', 'oo', 'oo', 'o|'])
        self.arr.append([' \\', 'oo', 'oo', '/ '])
        for i in range(randint(2, 4)):
            self.arr.append(['  ', '| ', ' |', '  '])
        self.arr.append(['  ', '|_', '_|', '  '])

    def action(self, player, map):
        print()
        if Constants.STONE_AXE not in player.inventory:
            print('You don\'t have an axe so you can\'t chop down the tree')
        else:
            print('What would you like to do?')
            print('1. Chop down the tree')
            print('2. Leave')
            try:
                x = input('-> ')
                if x == '1':
                    self.chop(player)
                    return True
                else:
                    return False
            except:
                print('Invalid input')
                return

    def chop(self, player):
        h = len(self.arr) - 5

        player.addItemToInventory(Constants.ACORN)
        for i in range(h):
            stickChance = randint(1, 100) % 2
            leafChance = randint(1, 100) % 3
            vineChance = randint(1, 100) % 5
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
        self.w = 35
        self.h = 27
        self.generateMine()

    def action(self, player, map):
        self.generateMineMap()
        self.player = player

        key = getkey()

        while key != 'q':
            key = getkey()

            x,y = self.pCoords
            if key == 'w' or key == keys.UP:
                self.movePlayer(x,y-1)
            elif key == 'a' or key == keys.LEFT:
                self.movePlayer(x-1,y)
            elif key == 's' or key == keys.DOWN:
                self.movePlayer(x,y+1)
            elif key == 'd' or key == keys.RIGHT:
                self.movePlayer(x+1,y)
    
    def generateMine(self):
        self.arr = []
        self.arr.append([' ╔', '══', '══', '══', '╗ '])
        self.arr.append([' ║', ' ╔', '══', '╗ ', '║ '])
        self.arr.append([' ║', ' ║', '  ', '║ ', '║ '])
        self.arr.append([' ║', ' ║', '  ', '║ ', '║ '])
        self.arr.append([' ║', ' ║', '  ', '║ ', '║ '])
        self.arr.append(['═╩', '═╩', '══', '╩═', '╩═'])

        self.generateMineMap()

    def generateMineMap(self):
        w = self.w
        h = self.h

        self.map = self.createFrame(w, h)

        default = '  '
        limit = 1000000000
        for i in range(h-1):
            for j in range(w-1):
                if i != 0 and i != h - 1 and j != 0 and j != w - 1:
                    num = randint(1, limit)
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

        x = int((self.h - 1) / 2)
        y = int((self.w + 1)/2)
        self.pCoords = (x,y)
        self.map[y][x] = Constants.PLAYER

    def display(self):
        window = [''.join(l) for l in self.map]
        window = '\n'.join(window)
        print(window)
        print(self.pCoords)

    def createFrame(self, w, h):
        frame = []

        top = [['╔'] + ['══' for i in range(w-2)] + ['╗']]
        bottom = [['╚'] + ['══' for i in range(w-2)] + ['╝']]

        frame = top + [(['║'] + ['  ' for i in range(w-2)] + ['║'])
                       for j in range(h-2)] + bottom

        return frame


    def getOre(self,character):
        if Constants.RED in character:
            return Constants.COPPER
        elif Constants.WHITE in character:
            return Constants.SILVER
        elif Constants.YELLOW in character:
            return Constants.GOLD
        elif Constants.MAGENTA in character:
            return Constants.AMETHYST
        elif Constants.GREEN in character:
            return Constants.JADE
        elif Constants.BLUE in character:
            return Constants.DIAMOND
    def movePlayer(self,x,y):
        oldx,oldy = self.pCoords
                

        if x > self.w - 2:
            x = self.w - 2
        elif x < 1:
            x = 1

        if y > self.h - 2:
            y = self.h - 2
        elif y < 1:
            y = 1

        self.pCoords = (x,y)
        
        
        character = self.map[y][x]

        if '.' in character or ':' in character:
            character = self.getOre(character)
            req = character.req
            
            if req not in self.player.inventory:
                self.pCoords = (oldx,oldy)
            else:
                self.player.addItemToInventory(character)

        if self.pCoords != (oldx,oldy):
            self.map[y][x] = Constants.PLAYER
            self.map[oldy][oldx] = '  '

            clearConsole()
            self.display()
        else:
            clearConsole()
            self.display()

        


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
