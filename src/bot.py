from player import Player

class Bot(Player):
    """Class Bot inherits from class Player and models a bot player using minimax/alpha-beta
    pruning algorithm to play against a human player or another bot player

    Attributes:
        same attr as base class
    """

    def __init__(self, name: str, sign: str):
        super().__init__(name, sign)
        self.__turn = False

    

    