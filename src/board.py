import constants

class GameBoard:
    """ Class GameBoard defines a 5x5 board for the game.

    Attributes:
        __board: board of the game
        __signed_slots: amount of taken slots in the board
"""

    def __init__(self):
        """Class constructore initializing board with empty cells
        """
        self.__board = [[" " for i in range(constants.BOARD_SIZE)] for i in range(constants.BOARD_SIZE)]
        self.__sigend_slots = 0
        self.is_max_turn = True
       
        

    def add_sign(self, x: int, y: int, value: str):
        """method for filling a board slot in positino x, y if it's empty
        Args:
            x (int): the x position of slot
            y (int): the y position of slot
            value (str): sign to be added into the slot
        
        Returns: 
            True if filled, otherwise False
        """

        
        if(self.__board[x][y] == " "):
            self.__board[x][y] = value
            self.__sigend_slots += 1
            return True

        else:
            raise ValueError(str(x) + " "+str(y) + " is invalid positions on the board!")
        
    def validate_positions(self, x: int, y: int):
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

    def remove_sign(self, x: int, y:int):
        if(x >= 0 and x < constants.BOARD_SIZE):
            if(y >= 0 and y < constants.BOARD_SIZE):
                self.__board[x][y] = " "
    
    def is_over(self, last_move: list):
        """Checks whether the game  has been ended in draw or win

        Args:
            last_move (list): [x, y] position of the last move
            max_turn (bool): who made the last move

        Returns:
            bool: True if game is over, False otherwise
        """
        if self.__sigend_slots == constants.BOARD_SIZE * constants.BOARD_SIZE:
            return True

        if self.__row_win(last_move) or self.__column_win(last_move):
            return True

        return False
        
    def free_neighbour_slots(self, x: int, y: int):
        neighbours = []

        #neighbour (-x,y)
        xUp = x-1
        if (xUp >= 0) and (self.__board[xUp][y] == " "):    
            neighbours.append((xUp, y))
            
        #neighbour (+x, y)
        xDown = x+1
        if (xDown < constants.BOARD_SIZE) and (self.__board[xDown][y] == " "):  
            neighbours.append((xDown, y))

        #neighbour (x, +y)
        yRight = y+1
        if(yRight < constants.BOARD_SIZE) and (self.__board[x][yRight] == " "):
            neighbours.append((x, yRight))

        #neighbour (x, -y)
        yLeft = y-1
        if(yLeft >= 0) and (self.__board[x][yLeft] == " "):
            neighbours.append((x, yLeft))

        #neighbour (-x, +y)
        xUpRight = x-1
        yUpRight = y+1
        if(xUpRight >= 0 and yUpRight < constants.BOARD_SIZE) and (self.__board[xUpRight][yUpRight] == " "):
            neighbours.append((xUpRight, yUpRight))


        #neighbour (+x, +y)
        xDownRight = x+1
        yDownRight = y+1
        if(xDownRight < constants.BOARD_SIZE and yDownRight < constants.BOARD_SIZE) and (self.__board[xDownRight][yDownRight] == " "):
            neighbours.append((xDownRight, yDownRight))

        #neighbour (-x, -y)
        xUpLeft = x-1
        yUpLeft = y-1
        if(xUpLeft >= 0 and yUpLeft >= 0) and (self.__board[xUpLeft][yUpLeft] == " "):
            neighbours.append((xUpLeft, yUpLeft))

        #neighbour (+x, -y)
        xDownLeft = x+1
        yDownLeft = y-1
        if(xDownLeft < constants.BOARD_SIZE and yDownLeft >= 0) and (self.__board[xDownLeft][yDownLeft] == " "):
            neighbours.append((xDownLeft, yDownLeft))
        
        return neighbours

    def __row_win(self, last_move):
        """This method checks if a winning row is found from the last move by a player

        Args:
            last_move (arr): x and y position of the last move on the board

        Returns:
            Boolean: True if a winning row found, False otherwise
        """ 
        x, y = last_move
        last_move_sign = self.__board[x][y]
        counter_left = 0

        #check for win in left direction from the last move
        while (y >= 0 and self.__board[x][y] == last_move_sign):
            counter_left += 1
            if counter_left == 5:
                return True
            y -= 1

        x, y = last_move
        counter_right = 0

         #check for win in right direction from the last move
        while(y < constants.BOARD_SIZE and self.__board[x][y] == last_move_sign):
            counter_right += 1
            if counter_right == 5:
                return True
            y += 1

        return ((counter_right + counter_left)-1) >= 5

    def __column_win(self, last_move):
        """_summary_

        Args:
            last_move (arr): x and y position of the last move

        Returns:
            Boolean: True if a winning column is found, False otherwise
        """
        x,y = last_move
        last_move_sign = self.__board[x][y]
        counter_up = 0
        #check for win going to up direction from the last move
        while(x >= 0 and self.__board[x][y] == last_move_sign):
            counter_up += 1
            if counter_up == 5:
                return True
            x -= 1

        x,y = last_move
        counter_down = 0
        #check for win going to down direction from the last move
        while((x < constants.BOARD_SIZE) and (self.__board[x][y] == last_move_sign)):
            counter_down += 1
            if counter_down == 5:
                return True
            x += 1

        return ((counter_down + counter_up)-1) >= 5

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