import constants

class GameBoard:
    """ Class GameBoard defines a 5x5 board for the game.

    Attributes:
        __board: board of the game
        __filled_slots: check and track filled board slots
"""

    def __init__(self):
        """Class constructore initializing board with empty cells
        """
        self.__board = [[" " for i in range(constants.BOARD_SIZE)] for i in range(constants.BOARD_SIZE)]
        self.__filled_slots = [[False for i in range(constants.BOARD_SIZE)] for i in range(constants.BOARD_SIZE)]
        self.__sigend_slots = 0
        self.__crosses_turn = False
        

    def fill_position(self, x: int, y: int, value: str):
        """method for filling a board slot in positino x, y if it's empty
        and mark that slot filled in the self.__filled_slots data structure

        Args:
            x (int): the x position of slot
            y (int): the y position of slot
            value (str): sign to be added into the slot
        
        Returns: 
            True if filled, otherwise False
        """

        
        if self.__validate_positions(x, y):
            if(not self.__filled_slots[x][y]):
                self.__board[x][y] = value
                self.__filled_slots[x][y] = True
                self.__sigend_slots += 1
                return True

        else:
            raise ValueError(str(x) + " "+str(y) + " is invalid positions on the board!")
        
    def is_end_state(self):
        return (self.__sigend_slots == (constants.BOARD_SIZE*constants.BOARD_SIZE)) or self.check_for_win()

    def generate_children(self):
        pass
    def is_max_node(self):
        return self.__crosses_turn

    def __validate_positions(self, x: int, y: int):
        """Private method validating the board positions. 

        Args:
            x (int): the x poistion of the board
            y (int): the y position of the board

        Returns:
            True if position is valid, otherwise False
        """

        if x>= 0 and x< constants.BOARD_SIZE:
            if y >= 0 and y < constants.BOARD_SIZE:
                return True
        return False


    def is_diagonal_win(self):
        """Check for a diagonal win in the board

        Retruns:
            True if all characters are the same diagonaly, otherwise False
        """
        row = []
        if self.__sigend_slots == 0:
            return False
        
        diagonal_win = True
        x = 0
        y = 0
        sign = self.__board[x][y]
        while x < constants.BOARD_SIZE and y < constants.BOARD_SIZE:
            sign_slot = self.__board[x][y]
            if sign_slot != sign or sign_slot == " ":
                diagonal_win = False
                return False
            else:
                row.append((x,y))
                x += 1
                y += 1

        if diagonal_win:
            return row

        row.clear()

        x = 0
        y = constants.BOARD_SIZE - 1
        sign = self.__board[x][y]
        while x < constants.BOARD_SIZE and y >= 0:
            sign_slot = self.__board[x][y]
            if sign_slot != sign or sign_slot == " ":
                return False
            else:
                row.append((x,y))
                x += 1
                y -= 1
        
        return row

    def is_row_win(self):
        """Check for possible win in a row in the board

        Returns:
            True if a row of the same sign found, otherwise False
        """
        won_rows = []
        if self.__sigend_slots == 0:
            return False
        
        for i in range(constants.BOARD_SIZE):
            sign = self.__board[i][0]
            won = True
            row = []
            for j in range(constants.BOARD_SIZE):
                if self.__board[i][j] != sign or self.__board[i][j] == " ":
                    won = False
                    break
                row.append((i,j))
            if won:
                won_rows.append(row)
    

        if len(won_rows) > 0:
            return won_rows
        else:
            return False

    def is_coloumn_win(self):
        won_columns = []
        if self.__sigend_slots == 0:
            return False

        for x in range(constants.BOARD_SIZE):
            row = []
            won = True
            sign = self.__board[x][0]
            for y in range(constants.BOARD_SIZE):
                if self.__board[y][x] != sign or self.__board[y][x] == " ":
                    won = False
                    break
                row.append((x, y))
            if won:
                won_columns.append(row)

        if len(won_columns) > 0:
            return won_columns
        else:
            return False

    def __str__(self):
        """Visualize the state of the board

        Returns:
            _type_: visualized board in string format
        """
        board_repr = ""
        for i in range(constants.BOARD_SIZE):
            for j in range(constants.BOARD_SIZE):
                board_repr += self.__board[i][j]
                board_repr += " | "
                
                

            board_repr += "\n"
            board_repr += "--- "*constants.BOARD_SIZE
            board_repr += "\n"
            
        return board_repr