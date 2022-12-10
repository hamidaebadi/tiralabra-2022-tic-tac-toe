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
        self.__winning_sign_amount = 5
       
        

    def add_mark(self, x: int, y: int, value: str):
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
                if self.__board[x][y] == " ":
                    return True
        raise ValueError()

    def remove_mark(self, x: int, y:int):
        self.__board[x][y] = " "
        self.__sigend_slots -= 1
    
    def is_winning(self, last_move: list):
        """Checks whether the game  has been ended in draw or win

        Args:
            last_move (list): [x, y] position of the last move
            max_turn (bool): who made the last move

        Returns:
            bool: True if game is over, False otherwise
        """
        if self.__row_win(last_move) or self.__column_win(last_move) or self.__clock_wise_diagnoal_win(last_move) or self.__anti_clock_wise_diagonal_win(last_move):
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
            if counter_left == self.__winning_sign_amount:
                return True
            y -= 1

        x, y = last_move
        counter_right = 0

         #check for win in right direction from the last move
        while(y < constants.BOARD_SIZE and self.__board[x][y] == last_move_sign):
            counter_right += 1
            if counter_right == self.__winning_sign_amount:
                return True
            y += 1

        return ((counter_right + counter_left)-1) >= self.__winning_sign_amount

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
            if counter_up == self.__winning_sign_amount:
                return True
            x -= 1

        x,y = last_move
        counter_down = 0
        #check for win going to down direction from the last move
        while((x < constants.BOARD_SIZE) and (self.__board[x][y] == last_move_sign)):
            counter_down += 1
            if counter_down == self.__winning_sign_amount:
                return True
            x += 1

        return ((counter_down + counter_up)-1) >= self.__winning_sign_amount

    def __clock_wise_diagnoal_win(self, last_move):
        xUpRight =last_move[0]
        yUpRight = last_move[1]
        last_move_mark = self.__board[xUpRight][yUpRight]
        counterUp = 0
        while (xUpRight >= 0 and yUpRight < constants.BOARD_SIZE) and self.__board[xUpRight][yUpRight] == last_move_mark:
            counterUp += 1
            if counterUp == self.__winning_sign_amount:
                return True
            xUpRight -= 1
            yUpRight += 1

        xDownLeft =last_move[0]
        yDownLeft = last_move[1]
        counterDonw = 0
        while (xDownLeft < constants.BOARD_SIZE and yDownLeft >= 0) and self.__board[xDownLeft][yDownLeft] == last_move_mark:
            counterDonw += 1
            if counterDonw == self.__winning_sign_amount:
                return True
            xDownLeft += 1
            yDownLeft -= 1

        return ((counterDonw + counterUp)-1) ==self.__winning_sign_amount

    def __anti_clock_wise_diagonal_win(self, last_move):
        xUpLeft = last_move[0]
        yUpLeft = last_move[1]
        last_move_mark = self.__board[xUpLeft][yUpLeft]
        counterUpLeft = 0
        while (xUpLeft >= 0 and yUpLeft >= 0) and self.__board[xUpLeft][yUpLeft] == last_move_mark:
            counterUpLeft += 1
            if counterUpLeft == self.__winning_sign_amount:
                return True
            xUpLeft -= 1
            yUpLeft -= 1


        xDownRight = last_move[0]
        yDownRight = last_move[1]
        counterDownRight = 0
        while(xDownRight < constants.BOARD_SIZE and yDownRight < constants.BOARD_SIZE) and self.__board[xDownRight][yDownRight] == last_move_mark:
            counterDownRight += 1
            if counterDownRight == self.__winning_sign_amount:
                return True

            xDownRight +=1
            yDownRight += 1

        return ((counterDownRight + counterUpLeft)-1)==self.__winning_sign_amount

    def draw(self):
        return self.__sigend_slots == (constants.BOARD_SIZE*constants.BOARD_SIZE)

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