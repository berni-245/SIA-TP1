from typing import Tuple
from anytree import Node
from sokoban import SokobanAction
from boards import board1, board2
from algorithms import search_algorithm, dfs
import sys
sys.setrecursionlimit(10000)
    
result: Tuple[Node, ...] = search_algorithm(
    board2.board,
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    dfs
)

print("DFS:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")