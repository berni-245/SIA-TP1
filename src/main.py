from typing import List, Tuple
from anytree import Node
from sokoban import Sokoban, SokobanBoard, SokobanAction, SokobanFieldType
from boards import board2
from algorithms import search_algorithm, bfs, dfs
import sys
sys.setrecursionlimit(10000)
    
# sokoban: Sokoban = Sokoban([board2])

result: Tuple[Node, ...] = search_algorithm(
    board2.board,
    board2.goals,
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    bfs
)

print("BFS:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")

# result: Tuple[Node] = search_algorithm(
    # board2.board,
    # board2.goals,
    # [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    # dfs
# )

# print("DFS:")
# for i, node in enumerate(result):
#     print(f"step: {i}")
#     print(node.name, "\n")
