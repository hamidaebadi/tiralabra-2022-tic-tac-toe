import constants

class Player:
    """ Class player modelling a player in the game

    Attributes:
        __name: name of the player
        __turn: is it player's turn to play

    """

    def __init__(self, name: str, sign: str):
        """Initialize player object data

        Args:
            name (str): name of the player
            sign (str): sign of the player on the board
            
        """
        self.__name = name
        self.__sign = sign
        self.__turn = True


    #getters and setters
    @property
    def name(self):
        return self.__name

    @property
    def sign(self):
        return self.__sign

    @property
    def turn(self):
        return self.__turn

    
    def swap_turn(self):
        self.__turn = not self.__turn

    def __str__(self):
        """Prints player's data to console
        """
        return f"Player's name: {self.__name} who plays with {self.__sign}"