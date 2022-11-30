class Player:
    """ Class player modelling a player in the game

    Attributes:
        __name: name of the player
        __turn: is it player's turn to play
        __occupied_rows: (int) number of rows a player has won

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
        self.__occupied_rows = 0
        self.__won_rows = []

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

    def add_win_row(self, row):
        if row not in self.__won_rows:
            print(f"Winning row: {row}")
            self.__won_rows.append(row)
            self.__occupied_rows += 1

    def won(self):
        return self.__occupied_rows == 2
    
    def swap_turn(self):
        self.__turn = not self.__turn

    def __str__(self):
        """Prints player's data to console
        """
        return f"Player's name: {self.__name} "