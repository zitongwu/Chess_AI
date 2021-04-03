"""
Author: Zitong Wu
Date: Oct 9, 2020

Description:
    Implement chess with minimax algorithm, alpha-beta pruning,
    cut-off test and iterative deepening search.

This Script: Test the chess game with various combinations of players.

A player can be a HumanPlayer, a RandomAI, a MinimaxAI, an AlphaBetaAI or
Iterative_Deepening_AI. 
"""

# pip3 install python-chess
import sys
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from Iterative_Deepening_AI import Iterative_Deepening_AI
from ChessGame import ChessGame
import time


# CREATE A PLAYER:
# specify the type: minimaxAI, alphabetaAI, or Iterative_Deepening_AI
# specify the depth limit: 1-5
# specify the color: chess.WHITE or chess.BLACK

player_human = HumanPlayer()
player_randomAI = RandomAI()

player_minimax_4_white = MinimaxAI(4, chess.WHITE)
player_minimax_4_black = MinimaxAI(4, chess.BLACK)
player_minimax_3_white = MinimaxAI(3, chess.WHITE)
player_minimax_3_black = MinimaxAI(3, chess.BLACK)
player_minimax_2_white = MinimaxAI(2, chess.WHITE)
player_minimax_2_black = MinimaxAI(2, chess.BLACK)
player_minimax_1_white = MinimaxAI(1, chess.WHITE)
player_minimax_1_black = MinimaxAI(1, chess.BLACK)

player_alphabeta_5_white = AlphaBetaAI(5, chess.WHITE)
player_alphabeta_5_black = AlphaBetaAI(5, chess.BLACK)
player_alphabeta_4_white = AlphaBetaAI(4, chess.WHITE)
player_alphabeta_4_black = AlphaBetaAI(4, chess.BLACK)
player_alphabeta_3_white = AlphaBetaAI(3, chess.WHITE)
player_alphabeta_3_black = AlphaBetaAI(3, chess.BLACK)
player_alphabeta_2_white = AlphaBetaAI(2, chess.WHITE)
player_alphabeta_2_black = AlphaBetaAI(2, chess.BLACK)
player_alphabeta_1_white = AlphaBetaAI(1, chess.WHITE)
player_alphabeta_1_black = AlphaBetaAI(1, chess.BLACK)

player_ids_4_white = Iterative_Deepening_AI(4, chess.WHITE)


# Make sure player1 in ChessGame(player1, player2) is set as white,
# and player2 is set as black

# Example: alphabetaAI with depth 3 (white) vs. alphabetaAI with depth 1 (black)
game = ChessGame(player_alphabeta_3_white , player_randomAI)

# Sets the board with a given fen string (i.e., fen representation of board positions)
# game.board.set_board_fen("rnbqkbn1/ppppppp1/8/7p/1PPPPP2/4r3/P5PP/RNBQKBNR")
# game.board.set_board_fen("r1bqk3/pppp4/2n1Pp2/PPP1P2p/5pn1/2N1r3/3b2PP/R1BQKBNR")
# game.board.set_board_fen("rb1qk3/pPpp4/4Pp2/P1P1n2p/5pn1/2b1B3/6PP/R1BQK1NR")

# Play the chess game
while not game.is_game_over():
    print(game)
    game.make_move()
    print(game)

# Print the game result
game.game_result()

