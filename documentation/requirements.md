# Introduction
Game has been the fundamental source of AI and it has been an old and well-defined problem in AI since the start
of AI concept. Well-defined, two-person games' algorithms have had huge impact on the development of AI. So, I decided
to impelemt Minimax and alpha-beta pruning algorithm in this course. In this page I lists all requirements for developing 
TIC-TAC-TOE game application. The main goal is to evaluate and document the efficiency of two algorithms used for developing 
this basic two-person, well-defined game. The algorithmes are MiniMax and alpha-beta pruning.

The main component of our game is a tree-state, which is the input of our program. Then the program will analyse it
and produce the best result, which could be the best possible next move in our game.

### Basic Info
* **Developer's Name:** *Hamid Aebadi*
* **Developer's Study Program:**  Bachelor's in Computer Science / TKT kandidaatti
* **Project's main language:** Python (Basic understanding of Java / C++)
* **Language used for documentation:** English


## Requirements
 - [ ] Program hires a bot to play tic-tac-toe with a human
 - [ ] Game is played in Terminal via commands 
 - [ ] human player start the game by telling the position in the board to add its mark
 - [ ] human plays with sign O
 - [ ] Bot plays with sign X
 - [ ] after each moves program prints the game state such as game board and possible winer
 - [ ] program can identify the winer 
 - [ ] program prints statics of the game at the end

# Algorithms' time and space complexity
 **MiniMax** 
    Time-complexity: Time complexity of the MiniMax algrothim is O(nm^3).