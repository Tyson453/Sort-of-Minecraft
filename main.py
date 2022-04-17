from code.game import Game
from code.structures import Tree, Mine
from code.constants import Constants

try:
    import cursor
    cursor.hide()
except:
    pass


mine = Mine()

items = [Constants.STICK, Constants.ROCK,
         Constants.LEAF, Constants.VINE]

game = Game(667, 375, 31, 19, items, .001, .0001)

game.play()
