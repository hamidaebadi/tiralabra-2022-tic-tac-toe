# Implementation documents

#### General program structure
 This application is designed by practicing Object-Oriented-Programming principles.
 Main components of the application are user interface being implemented in commandline format, business logic,
 configuration file and the main algorithm.

Program begins from main.py file by initializing the UI and then starting it.

**Classes for UI**
 - UserInteface

**Classes for buisiness logic**
 - GameBoard
 - Game
 - Player
 - Bot

**Configuration file**
 - constants.py is for configuring the application. For example, board size

#### Application's running flow
 - Application starts from main.py.
 - Prepare user interface for interacting with application
 - Create nxn board according to BOARD_SIZE constant in configuration file
 - Create a human player and a bot player
 - Create a game object which requires already defined board, and players objects
 - start the game
 - continue till game ends (by winning 5 rows if board is 25x25 / Draw)



##### Improvements needed?
 - A lot of code refactoring is needed
 - more functionality in business logic