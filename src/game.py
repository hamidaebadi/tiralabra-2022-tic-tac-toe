class Game:
    """Class Game models and implement the tic-tac-toe game

    Attributes:
        __game_board: an object of class GameBoard
        __player: an object of class Player
    """
    def __init__(self, board, player1, player2):
        self.__game_board = board
        self.__player1 = player1
        self.__player2 = player2


    def __is_over(self):
        """This method check if the game is over

        Retruns:
            True if a win found, otherwise False
        """

        if self.__player1.won() or self.__player2.won():
            return True
        return False

    def start(self):
        print(f"Game started between {self.__player1.name} and {self.__player2.name}")
        print(self.__game_board)
        while not self.__is_over():
            if(self.__player1.turn):    #it's human's turn
                positions = [int(num) for num in input("Your Turn! \n Where to put your sign: ").split()]
                if len(positions) == 0:
                    break
                try:
                    self.__game_board.fill_position(positions[0], positions[1], self.__player1.sign)
                except ValueError:
                    print("Incorrect board positions were given!")
                    print("Try again")
                    continue

                row = self.__game_board.is_diagonal_win()

                if row:
                    self.__player1.add_win_row(row)


                rows = self.__game_board.is_row_win()
                if rows:
                    for row in rows:
                        self.__player1.add_win_row(row)


                rows = self.__game_board.is_coloumn_win()
                print(f"column {row}")
                if rows:
                    for row in rows:
                        self.__player1.add_win_row(row)
                
            
                print("Board state: ")
                print(self.__game_board)
                self.__player1.swap_turn()
                self.__player2.swap_turn()
                
            else:
                #bot plays
                print("Bot Plays a move")
                #alogrithm works here
                self.__player2.swap_turn()
                self.__player1.swap_turn()
            


    