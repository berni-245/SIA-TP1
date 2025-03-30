import sys
import time
import argparse

from src.sokoban import SokobanAction, SokobanBoard
from src.algorithms import algorithms, search_algorithm

sys.setrecursionlimit(10000)

parser = argparse.ArgumentParser(description="Process a board file using a specified algorithm and save the output.")

# Define expected arguments
parser.add_argument("algorithm", choices=algorithms.keys(), help="The algorithm to use.")
parser.add_argument("board_file", help="Path to the board file")
parser.add_argument("output_file", help="Path to save the output")

# Parse arguments
args = parser.parse_args()

with open(args.board_file, "r") as f:
    board_string = f.read()

start_time = time.time()

result = search_algorithm(
    SokobanBoard.board_builder(board_string),
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    algorithms[args.algorithm.lower()]
)

elapsed_time = time.time() - start_time

with open(args.output_file, "w") as f:
        f.write(f"-------- {args.algorithm.upper()} --------\n\n")
        f.write(f"Time taken: {elapsed_time:.6f} seconds\n\n")
        for i, node in enumerate(result):
            f.write(f"step: {i}\n")
            f.write(f"{node.name}\n\n")
