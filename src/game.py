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
        print(self.__game_board)
        while not self.__game_board.check_for_win():
            if(self.__player1.turn):
                positions = [int(num) for num in input("Your Turn! \n Where to put your sign: ").split()]
                if len(positions) == 0:
                    break
                try:
                    self.__game_board.fill_position(positions[0], positions[1], self.__player1.sign)
                except ValueError:
                    print("Add to correct slot!")
                    continue
            
                print("Board state: ")
                print(self.__game_board)
                self.__player1.swap_turn()
                self.__player2.swap_turn()
                
            else:
                print("Bot Played a move")
                self.__player2.swap_turn()
                self.__player1.swap_turn()
            


    