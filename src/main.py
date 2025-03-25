from typing import List
from sokoban import Sokoban, SokobanBoard, SokobanFieldType, SokobanAction

board_matrix: List[List[SokobanFieldType]] = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.PLAYER, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.BOX, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]
    
board: SokobanBoard = SokobanBoard(board_matrix)
sokoban: Sokoban = Sokoban([board])

print(sokoban.get_board()
      )
print(SokobanAction.DOWN)
sokoban.execute_action(SokobanAction.DOWN)
print(sokoban.get_board())

print(SokobanAction.LEFT)
sokoban.execute_action(SokobanAction.LEFT)
print(sokoban.get_board())

print(SokobanAction.RIGHT)
sokoban.execute_action(SokobanAction.RIGHT)
print(sokoban.get_board())

print(SokobanAction.UP)
sokoban.execute_action(SokobanAction.UP)
print(sokoban.get_board())

print(SokobanAction.RIGHT)
sokoban.execute_action(SokobanAction.RIGHT)
print(sokoban.get_board())

print(SokobanAction.DOWN)
sokoban.execute_action(SokobanAction.DOWN)
print(sokoban.get_board())


