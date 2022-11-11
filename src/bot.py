class Bot:
    """Class Bot models a bot player using minimax/alpha-beta
    pruning algorithm to play against a human player or another bot player

    Attributes:
        self.__name: constatnt name of the bot player
    """

    def __init__(self, name: str):
        self.__NAME = name

    #getter and setters
    @property
    def name(self):
        return self.__NAME

    

    