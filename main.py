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

try:
    import cursor
    cursor.hide()
except:
    pass


# mine = Mine()

# mine.action()

# mine.display()


items = [Constants.STICK, Constants.ROCK,
         Constants.LEAF, Constants.VINE]

game = Game(32, 32, 31, 19, items, .001, .001)

game.play()
