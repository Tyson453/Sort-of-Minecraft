try:
    from code import util
    from code.game import Game
    from code.structures import Tree, Mine
    from code.constants import Constants
except:
    from game import Game
    from structures import Tree, Mine
    from constants import Constants

try:
    import cursor
    cursor.hide()
except:
    pass


mine = Mine()

items = [Constants.STICK, Constants.ROCK,
         Constants.LEAF, Constants.VINE]

game = Game(32, 32, 31, 19, items, .002, .002)

game.play()

# mine.action(game.player,game.map)
