from minimax import minimax
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
        last_move=[]
        while True:
            if(self.__player1.turn):    #it's human's turn
                positions = [int(num) for num in input("Your Turn! \n Where to put your sign: ").split()]
                last_move = positions
                if len(positions) == 0:
                    break
                try:
                    if self.__game_board.validate_positions(positions[0], positions[1]):
                        self.__game_board.add_sign(positions[0], positions[1], self.__player1.sign)
                    if(self.__game_board.is_over(positions)):
                        break
                except ValueError:
                    print("Incorrect board positions were given!")
                    print("Try again")
                    continue

            
                print("Board state: ")
                print(self.__game_board)
                self.__player1.swap_turn()
                self.__player2.swap_turn()
                
            else:
                #bot plays
                print("Bot Plays a move")
                #alogrithm works here
                moves_list = set()
                neighbours = self.__game_board.free_neighbour_slots(last_move[0], last_move[1])
                for item in neighbours:
                    moves_list.add((item[0], item[1]))
                move = minimax(self.__game_board, last_move, moves_list, True, 0)
                print(move)
                self.__player2.swap_turn()
                self.__player1.swap_turn()
        print("Game ended in the following state")
        print(self.__game_board)
            


    