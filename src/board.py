class GameBoard:
    """ Class GameBoard defines a 3x3 board for the game.

    Attributes:
        __board: board of the game
        __filled_slots: check and track empty board slots
"""

    def __init__(self):
        """Class constructore initializing board with empty cells
        """
        self.__board = [["" for i in range(3)] for i in range(3)]
        self.__filled_slots = [[False for i in range(3)] for i in range(3)]
        

    def fill_position(self, x: int, y: int, value: str):
        """method for filling a board slot in positino x, y if it's empty
        and mark that slot filled in the self.__filled_slots data structure

        Args:
            x (int): the x position of slot
            y (int): the y position of slot
            x (str): sign to be added into the slot
        
        Returns: 
            True if filled, otherwise False
        """

        if(not self.__filled_slots[x][y]):
            self.__board[x][y] = value
            self.__filled_slots[x][y] = True
            return True

        return False
        


    def __str__(self):
        """Visualize the state of the board

        Returns:
            _type_: visualized board in string format
        """
        board_repr = ""
        for i in range(3):
            for j in range(3):
                board_repr += self.__board[i][j]
                board_repr += " | "

            board_repr += "\n"
            board_repr += "--- --- ---"
            board_repr += "\n"
            
        return board_repr