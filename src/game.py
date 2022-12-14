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
        moves_list = set()
        while True:
            if(self.__player1.turn):    #it's human's turn
                positions = [int(num) for num in input("Your Turn! \n Where to put your sign: ").split()]
                last_move = positions
                if len(positions) == 0:
                    break
                try:
                    if self.__game_board.validate_positions(positions[0], positions[1]):
                        self.__game_board.add_mark(positions[0], positions[1], self.__player1.sign)
                    if(self.__game_board.is_winning(positions)):
                        break
                except ValueError:
                    print("Illegal move")
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
                neighbours = self.__game_board.free_neighbour_slots(last_move[0], last_move[1])
                for item in neighbours:
                    moves_list.add(item)
                if (last_move[0], last_move[1]) in moves_list:
                    moves_list.remove((last_move[0], last_move[1]))
                        
                print(moves_list)
                result = minimax(self.__game_board, last_move, moves_list, True, float("-inf"), float("+inf"), 7)
                best_move = result[1]
                self.__game_board.add_mark(best_move[0], best_move[1], self.__player2.sign)
                if (best_move[0], best_move[1])in moves_list:
                    moves_list.remove((best_move[0], best_move[1]))
                print(self.__game_board)
                if(self.__game_board.is_winning(best_move) or self.__game_board.is_draw()):
                    break
                self.__player2.swap_turn()
                self.__player1.swap_turn()
        print("Game ended in the following state")
        print(self.__game_board)
            


    