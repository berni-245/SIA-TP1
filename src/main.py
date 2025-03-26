from typing import List, Tuple
from anytree import Node
from sokoban import Sokoban, SokobanBoard, SokobanFieldType, SokobanAction
from algorithms import search_algorithm, bfs, dfs

board_matrix: List[List[SokobanFieldType]] = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.PLAYER, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.BOX, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]

goal_matrix1: List[List[SokobanFieldType]] = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.PLAYER, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.BOX_ON_GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]

goal_matrix2: List[List[SokobanFieldType]] = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.PLAYER, SokobanFieldType.BOX_ON_GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]
    
board: SokobanBoard = SokobanBoard(board_matrix)
goal1: SokobanBoard = SokobanBoard(goal_matrix1)
goal2: SokobanBoard = SokobanBoard(goal_matrix2)
sokoban: Sokoban = Sokoban([board])

result: Tuple[Node] = search_algorithm(
    board,
    [goal1, goal2],
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    bfs
)

print("BFS:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")

result: Tuple[Node] = search_algorithm(
    board,
    [goal1, goal2],
    [SokobanAction.UP, SokobanAction.DOWN, SokobanAction.LEFT, SokobanAction.RIGHT],
    dfs
)

print("DFS:")
for i, node in enumerate(result):
    print(f"step: {i}")
    print(node.name, "\n")