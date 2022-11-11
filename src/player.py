class Player:
    """ Class player modelling a player in the game

    Attributes:
        __name: name of the player
        
    """

    def __init__(self, name: str):
        """Initialize player object data

        Args:
            name (str): name of the player
        """
        self.__name = name

    #getters and setters
    @property
    def name(self):
        return self.__name


    def __str__(self):
        """Prints player's data to console
        """
        return f"Player's name: {self.__name} "