from typing import Tuple
from anytree import Node
from sokoban import SokobanAction, SokobanBoard
# from boards import board1, board2
from algorithms import a_star, heuristic_manhatan, search_algorithm, dfs, bfs, greedy
import sys
sys.setrecursionlimit(10000)

# board_str = """
# ####  ######
# #  #  #   g#
# #  ####    #
# #    g    b#
# # p    b   #
# #        ###
# ##########      
# """

# board_str = """
# ####
# #g #
# #  ##
# # b #
# # p #
# #  #
# ####
# """

# board_str = """
# #############
# #           #
# #  b        #
# #           #
# #     p     #
# #          g#
# #############
# """

board_str = """
##########################
#######g##################
#######g#######  #########
###         ##   #########
##  # # # #         g#####
#  ##     ##  # ##########
# ##  # #  ## # ##########
#     bpb     #   b ######
####  ###  ####     ######
##########################
"""

# board_str = """
# ###############
# #######g#######
# #######g#######
# ###         ###
# ##  # # # #  ##
# #  ##     ##  #
# # ##  # #  ## #
# #     bpb     #
# ####  ###  ####
# ###############
# """

board = SokobanBoard.board_builder(board_str)

import time

start_time = time.time()

result: Tuple[Node, ...] = search_algorithm(
    board,
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    a_star
)

end_time = time.time()
elapsed_time = end_time - start_time

print("Greedy 2:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")

print(f"Elapsed time: {elapsed_time:.4f} seconds")
