from typing import Tuple
from anytree import Node
from src.sokoban import SokobanAction, SokobanBoard
from src.algorithms import algorithms, search_algorithm
import sys
import json
import time
sys.setrecursionlimit(10000)


with open("configs/config.json", "r") as f:
    config = json.load(f)

with open("boards/"+ config["board"] + ".txt", "r") as f:
    board_string = f.read()

start_time = time.time()

result, expanded_nodes, remaining_nodes, max_nodes = search_algorithm(
    SokobanBoard.board_builder(board_string),
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    algorithms[config["algorithm"].lower()]
)

elapsed_time = time.time() - start_time

result_file_name = f'{config['algorithm']}-{config['board']}-drlu.txt'
with open(f"results/{result_file_name}", "w") as f:
        f.write(config["algorithm"].lower() + ":\n")
        f.write(f"Time taken: {elapsed_time:.6f} seconds\n")
        f.write(f"Expanded frontier nodes: {expanded_nodes}\n")
        f.write(f"Remaining frontier nodes: {remaining_nodes}\n")
        f.write(f"Max frontier nodes: {max_nodes}\n")
        for i, node in enumerate(result):
            f.write(f"step: {i}\n")
            f.write(f"{node.name}\n\n")
