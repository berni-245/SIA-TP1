from typing import Tuple
from anytree import Node
from sokoban import SokobanAction
from boards import board1, board3
from algorithms import search_algorithm, dfs, bfs
import sys
sys.setrecursionlimit(10000)
    
print(board3)
result: Tuple[Node, ...] = search_algorithm(
    board3,
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    bfs
)

print("BFS:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")