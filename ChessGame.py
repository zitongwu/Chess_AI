"""
Author: Zitong Wu
Date: Oct 9, 2020

Description:
    Implement a chess A.I. with minimax algorithm, alpha-beta pruning,
    cut-off test and iterative deepening search.

This Script: Models the chess game (provided code).
"""

import chess
import random

class ChessGame:
    def __init__(self, player1, player2):
        self.board = chess.Board()
        self.players = [player1, player2]

    def make_move(self):
        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)

        self.board.push(move)  # Make the move

    def is_game_over(self):
        return self.board.is_game_over()

    def game_result(self):
        # Prints the game result
        if self.board.is_checkmate():
            if self.board.turn == 1:
                print("The black wins")
            else:
                print("The white wins")
        elif self.board.is_stalemate():
            print("Stalemate")
        elif self.board.is_insufficient_material():
            print("Insufficient material")
        elif self.board.is_seventyfive_moves():
            print("Seventyfive moves")
        else:
            print("Other types of draw")

    def total_move_number(self):
        """Returns the number of total moves made for the game"""
        num_total_move = (self.board.fullmove_number - 1) * 2
        if self.board.turn == 0:
            num_total_move += 1
        return num_total_move

    def __str__(self):

        column_labels = "\n----------------\na b c d e f g h\n"
        board_str =  str(self.board) + column_labels

        # did you know python had a ternary conditional operator?
        move_str = "White to move" if self.board.turn else "Black to move"

        return board_str + "\n" + move_str + "\n"
