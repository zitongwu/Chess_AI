"""
Author: Zitong Wu
Date: Oct 9, 2020

This Script: Models a random chess player that takes a random move from the list of legal moves.
"""

#import chess
import random
from time import sleep

class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)
        sleep(1)   # I'm thinking so hard.
        print("Random AI recommending move " + str(move))
        return move
