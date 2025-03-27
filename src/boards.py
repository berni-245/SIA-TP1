from sokoban import SokobanFieldType, SokobanBoard

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



board1 = SokobanBoard.board_builder(board1_matrix)

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

board2 = SokobanBoard.board_builder(board2_matrix)

#----------------------------------------------------------------
# BOARD 3

#----------------------------------------------------------------
# BOARD 4

#----------------------------------------------------------------
# BOARD 5

