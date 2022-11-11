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

    def start(self):
        print(f"Game started between {self.__player1.name} and {self.__player2.name}")
        print("Board current state: ")
        print(self.__game_board)



    