from typing import Tuple
from anytree import Node
from sokoban import SokobanAction, SokobanBoard
from algorithms import search_algorithm, dfs, bfs, greedy_euc, greedy_man, greedy_corners, greedy_no_dead, a_star_euclidean, a_star_manhatan, a_star_manhatan_corners, a_star_manhatan_no_dead
import sys
import json
import time
sys.setrecursionlimit(10000)

algorithms = {"bfs": bfs,
              "dfs": dfs,
              "greedy_euc": greedy_euc,
              "greedy_man": greedy_man,
              "greedy_no_corners": greedy_corners,
              "greedy_no_dead": greedy_no_dead,
              "a*_euc": a_star_euclidean,
              "a*_man": a_star_manhatan,
              "a*_no_corners": a_star_manhatan_corners,
              "a*_no_dead": a_star_manhatan_no_dead,
              }


with open("configs/config.json", "r") as f:
    config = json.load(f)

with open("boards/"+ config["board"] + ".txt", "r") as f:
    board_string = f.read()

start_time = time.time()

result: Tuple[Node, ...] = search_algorithm(
    SokobanBoard.board_builder(board_string),
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    algorithms[config["algorithm"].lower()]
)

elapsed_time = time.time() - start_time

with open("result.txt", "w") as f:
        f.write(config["algorithm"].lower() + ":\n")
        f.write(f"Time taken: {elapsed_time:.6f} seconds\n")
        for i, node in enumerate(result):
            f.write(f"step: {i}\n")
            f.write(f"{node.name}\n\n")