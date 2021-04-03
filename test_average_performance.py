"""
Author: Zitong Wu
Date: Oct 9, 2020

Description:
    Implement chess with minimax algorithm, alpha-beta pruning,
    cut-off test and iterative deepening search.

This Script: Tests the average number of moves in a game by two players. 

A player can be a HumanPlayer, a RandomAI, a MinimaxAI, an AlphaBetaAI or
Iterative_Deepening_AI. 
"""

import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from Iterative_Deepening_AI import Iterative_Deepening_AI
from ChessGame import ChessGame

# CREATE A PLAYER:
# specify the type: minimaxAI, alphabetaAI, or Iterative_Deepening_AI
# specify the depth limit: 1-5
# specify the color: chess.WHITE or chess.BLACK

player_human = HumanPlayer()
player_randomAI = RandomAI()

player_minimax_3_white = MinimaxAI(3, chess.WHITE)
player_minimax_3_black = MinimaxAI(3, chess.BLACK)
player_minimax_2_white = MinimaxAI(2, chess.WHITE)
player_minimax_2_black = MinimaxAI(2, chess.BLACK)
player_minimax_1_white = MinimaxAI(1, chess.WHITE)
player_minimax_1_black = MinimaxAI(1, chess.BLACK)

player_alphabeta_4_white = AlphaBetaAI(4, chess.WHITE)
player_alphabeta_4_black = AlphaBetaAI(4, chess.BLACK)
player_alphabeta_3_white = AlphaBetaAI(3, chess.WHITE)
player_alphabeta_3_black = AlphaBetaAI(3, chess.BLACK)
player_alphabeta_2_white = AlphaBetaAI(2, chess.WHITE)
player_alphabeta_2_black = AlphaBetaAI(2, chess.BLACK)
player_alphabeta_1_white = AlphaBetaAI(1, chess.WHITE)
player_alphabeta_1_black = AlphaBetaAI(1, chess.BLACK)

player_ids_3_white = Iterative_Deepening_AI(3, chess.WHITE)

num_trials = 20
num_moves = 0
for i in range(num_trials):
    game = ChessGame(player_alphabeta_3_white, player_alphabeta_1_black)
    print(game)
    while not game.is_game_over():
        game.make_move()
    game.game_result()
    num_moves += game.total_move_number()
    print("Total number of moves in this game: ", end="")
    print(game.total_move_number())
    print()
print("Average number of moves in a game: ", end="")
print(num_moves/20)

