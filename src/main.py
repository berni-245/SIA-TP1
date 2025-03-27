from typing import Tuple
from anytree import Node
from sokoban import SokobanAction, SokobanBoard
from algorithms import search_algorithm, dfs, bfs
import sys
import json
sys.setrecursionlimit(10000)

algorithms = {"bfs": bfs,
              "dfs": dfs}


with open("configs/config.json", "r") as f:
    config = json.load(f)

with open("boards/"+ config["board"] + ".txt", "r") as f:
    board_string = f.read()

result: Tuple[Node, ...] = search_algorithm(
    SokobanBoard.board_builder(board_string),
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    algorithms[config["algorithm"].lower()]
)

with open("result.txt", "w") as f:
        f.write(config["algorithm"].lower() + ":\n")
        for i, node in enumerate(result):
            f.write(f"step: {i}\n")
            f.write(f"{node.name}\n\n")