from game import Game
from board import GameBoard
from bot import Bot
from player import Player

class UserInterface:
    """Class UserInterface provides easier usage of the program in the console

    Attributes:
    
    """

    def __init__(self):
        pass

    def start():
        print("Welcome to TicTacToe Game!")
        print("Commands: ")
        print("""
        1- start : Start the game
        2- exit: quite the program
        """)
        while(True):
            cmd = input("Enter a command: ")
            
            if(cmd == "exit"):
                print("Good bye!")
                break
            
            if(cmd == "start"):
                #prepare the game
                #create board and player
                pl1_name = input("What is your name? ")
                bot_name = input("Choose a name for your opponent: ")
                tictactoe_board = GameBoard()
                human_player = Player(name=pl1_name, sign="X")
                bot_player = Bot(name=bot_name, sign="O")
                game = Game(tictactoe_board, human_player, bot_player)
                game.start()
                
            