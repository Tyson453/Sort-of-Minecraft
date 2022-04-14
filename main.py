try:
    from code.map import Map
    from code import util
    from code.game import Game
    from code.structures import Tree, Mine
    from code.constants import Constants
except:
    from map import Map
    import util
    from game import Game
    from structures import Tree, Mine
    from constants import Constants


import cursor

cursor.hide()

mine = Mine()

mine.display()


# items = [Constants.ITEMS.FLOOR.STICK, Constants.ITEMS.FLOOR.STONE,Constants.ITEMS.FLOOR.LEAF,Constants.ITEMS.FLOOR.VINE]

# game = Game(32,32,31,19,items,.001, .000025)

# game.play()
