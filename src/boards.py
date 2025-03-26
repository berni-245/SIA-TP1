from sokoban import SokobanFieldType, SokobanBoard
from typing import List

#----------------------------------------------------------------
# BOARD 1

class SokobanInfoBoard:
    def __init__(self, initial_board, goal_boards):
        self.board = initial_board
        self.goals = goal_boards

board1_matrix = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.PLAYER, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.BOX, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]

board1_goal1_matrix = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.PLAYER, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.BOX_ON_GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]

board1_goal2_matrix = [
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.PLAYER, SokobanFieldType.BOX_ON_GOAL, SokobanFieldType.WALL],
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL]
]



board1 = SokobanInfoBoard(
    initial_board = SokobanBoard(board1_matrix),
    goal_boards = [SokobanBoard(board1_goal1_matrix), SokobanBoard(board1_goal2_matrix)]
)

#----------------------------------------------------------------
# BOARD 2

board2_matrix = [
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.GOAL,  SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.GOAL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.BOX,  SokobanFieldType.PLAYER,  SokobanFieldType.BOX,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.WALL]
]

board2_goal_matrix = [
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.BOX_ON_GOAL,  SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.BOX_ON_GOAL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.PLAYER,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL],
    
    [SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.AIR, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.WALL, SokobanFieldType.WALL],
    
    [SokobanFieldType.AIR,  SokobanFieldType.AIR, SokobanFieldType.AIR, SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.AIR,  SokobanFieldType.WALL,  SokobanFieldType.WALL,  SokobanFieldType.WALL, SokobanFieldType.WALL]
]

board2 = SokobanInfoBoard(
    initial_board = SokobanBoard(board2_matrix),
    goal_boards = [SokobanBoard(board2_goal_matrix)]
)

#----------------------------------------------------------------
# BOARD 3

#----------------------------------------------------------------
# BOARD 4

#----------------------------------------------------------------
# BOARD 5

