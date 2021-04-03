"""
Author: Zitong Wu
Date: Oct 9, 2020

Description:
    Implement chess with minimax algorithm, alpha-beta pruning,
    cut-off test and iterative deepening search.

This Script: Implements the minimax algorithm with alpha-beta pruning and cut-off test.
"""

import chess
from math import inf
import random
import time

class AlphaBetaAI():

    def __init__(self, depth_limit, color):
        self.depth_limit = depth_limit
        self.color = color
        self.num_calls = 0
        self.num_max_calls = 0

    def choose_move(self, board):
        """Returns one of the best moves for AlphaBetaAi"""

        # Print the total move number up until now
        total_move_number = self.total_move_number(board)
        print("Total number of moves: ", end="")
        print(total_move_number)

        start_time = time.time()
        self.num_calls = 0
        best_value, best_move = self.alpha_beta_search(board)
        end_time = time.time()
        time_used = end_time - start_time

        print("AlphabetaAI of depth " + str(self.depth_limit) + ", " + ("White" if self.color else "BLACK"))
        print("time used: " + str(time_used))
        print("best value: ", end="")
        print(best_value)
        print("best move: ", end="")
        print(best_move)
        print("Number of calls of minimax: " + str(self.num_calls))
        return best_move

    def total_move_number(self, board):
        """Returns the number of total moves made for a given board"""
        num_total_move = (board.fullmove_number - 1) * 2
        if board.turn == 0:
            num_total_move += 1
        return num_total_move

    def cutoff_test(self, board, test_depth):
        """Returns True if the search should be cut off,
        either because it reaches the specified depth limit,
        or the game is over"""
        if board.is_game_over() or test_depth > self.depth_limit:
            return True
        return False

    def alpha_beta_search(self, board):
        """Returns the best evaluation value and move
         found from the alpha_beta search"""
        self.num_max_calls = 0
        v, best_move = self.max_value(board, -inf, inf, 0)
        return v, best_move

    def max_value(self, board, alpha, beta, test_depth):
        """Returns the best evaluation value and move
        found for a max node"""
        test_depth += 1
        self.num_calls += 1
        self.num_max_calls += 1

        if self.cutoff_test(board, test_depth):
            return self.evaluation(board), None

        v = -inf
        best_move = None
        moves = list(board.legal_moves)
        # Shuffles the list of legal moves for the first max node, i.e., the root node
        if self.num_max_calls == 1:
            random.shuffle(moves)
        # Sort the moves by their heuristic values in decreasing order

        for move in moves:
            board.push(move)
            current_min_value = self.min_value(board, alpha, beta, test_depth)
            board.pop()
            if current_min_value > v:
                v = current_min_value
                best_move = move
            if v >= beta:
                return v, best_move
            alpha = max(alpha, v)
        return v, best_move

    def min_value(self, board, alpha, beta, test_depth):
        """Returns the best evaluation value found for a min node
        ("best" from the perspective of the min node)"""
        test_depth += 1
        self.num_calls += 1
        if self.cutoff_test(board, test_depth):
            return self.evaluation(board)
        v = inf
        moves = list(board.legal_moves)
        for move in moves:
            board.push(move)
            current_max_value = self.max_value(board, alpha, beta, test_depth)[0]
            board.pop()
            if current_max_value < v:
                v = current_max_value
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def material_value(self, type):
        """Returns the material value for a given piece type"""
        if type == 1:
            value = 1
        elif type == 2 or type == 3:
            value = 3
        elif type == 4:
            value = 5
        elif type == 5:
            value = 9
        else:
            value = 0
        return value

    def evaluation(self, board):
        """Returns the evaluation value for a given board"""
        value = 0

        # Increase the evaluation value by 100 if AlphabetaAI
        #checkmates the opponent, otherwise decreases the evaluation
        #value by 100
        if board.is_checkmate():
            if board.turn != self.color:
                value = 100
            else:
                value = -100

        # Sums the material values of all the pieces left for AlphabetaAI
        # and then minus the material values of all the pieces left for the opponent
        for square in board.piece_map():
            type = board.piece_type_at(square)
            color = board.color_at(square)
            if color == self.color:
                value += self.material_value(type)
            else:
                value -= self.material_value(type)
        return value


