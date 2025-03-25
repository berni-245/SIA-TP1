from state import State, Action
from enum import Enum
from typing import List, Tuple
from copy import deepcopy

class SokobanFieldType(Enum):
    AIR = ("Air"),
    WALL = ("Wall"),
    PLAYER = ("Player"),
    BOX = ("Box"),
    GOAL = ("Goal"),
    PLAYER_ON_GOAL = ("Player On Goal"),
    BOX_ON_GOAL = ("Box On Goal")

    def __init__(self, name: str):
        self._name = name

class SokobanAction(Action, Enum):
    UP = (
        "Up action",
        lambda board: generic_transition_func(board, 0, 1), 
        lambda board: generic_can_run_action(board, 0, 1),
        1
    )
    DOWN = (
        "Down action",
        lambda board: generic_transition_func(board, 0, -1), 
        lambda board: generic_can_run_action(board, 0, -1),
        1
    )
    LEFT = (
        "Left action",
        lambda board: generic_transition_func(board, -1, 0), 
        lambda board: generic_can_run_action(board, -1, 0),
        1
    )
    RIGHT = (
        "Right action",
        lambda board: generic_transition_func(board, 1, 0), 
        lambda board: generic_can_run_action(board, 1, 0),
        1
    )
    
class SokobanBoard(State):
    def __init__(self, board: List[List[SokobanFieldType]]):
        if not board or not all(isinstance(row, list) for row in board):
            raise ValueError("Board must be a 2D list of SokobanFieldType values")
        super().__init__(board)
    
    def get_field(self, row_index: int, col_index: int) -> SokobanFieldType:
        return self.value[row_index][col_index]
    
    def set_field(self, row_index: int, col_index: int, field: SokobanFieldType) -> None:
        self.value[row_index][col_index] = field

    # REVISAR: Si es mejor tener constantemente actualizada la posición del jugador en una variable adicional.
    def find_player(self) -> Tuple[int, int]:
        for row_index, row in enumerate(self._value):
            for col_index, field in enumerate(row):
                if field == SokobanFieldType.PLAYER or field == SokobanFieldType.PLAYER_ON_GOAL:
                    return (row_index, col_index)
        raise ValueError("No player was found")
    
    def get_hard_copy(self):
        to_return: List[List[SokobanFieldType]] = deepcopy(self.value)
        return SokobanBoard(to_return)


class Sokoban:
    def __init__(self, boards_list: List[SokobanBoard]):
        if len(boards_list) == 0:
            raise RuntimeError("You must provide at least one board")
        self._boards_list = boards_list
        self._current_board: SokobanBoard = boards_list[0]
        self._index = 0

    def has_next_board(self) -> bool:
        return self._index < len(self._boards_list) - 1

    def next_board(self):
        if(not self.has_next_board()):
            raise RuntimeError("There' no more boards available")
        self._index += 1
        self._current_board = self._boards_list[self._index]
        return self


    def execute_action(self, action: SokobanAction):
        return action.execute(self._current_board)
        
    def get_board(self):
        return self._current_board.get_hard_copy()
    
    def set_current_board(self, new_board: SokobanBoard):
        self._current_board = new_board
        return self
    
def generic_can_run_action(board: SokobanBoard, x_inc: int, y_inc: int) -> bool:
    player_pos: Tuple = board.find_player()
    field_incremented: SokobanFieldType = board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    if(field_incremented == SokobanFieldType.WALL):
        return False
    
    # If there's a box, verify that the player can actually move the box
    if(field_incremented == SokobanFieldType.BOX or field_incremented == SokobanFieldType.BOX_ON_GOAL):
        field_double_incremented: SokobanFieldType = board.get_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        if not (field_double_incremented == SokobanFieldType.AIR or field_double_incremented == SokobanFieldType.GOAL):
            return False
    return True

def generic_transition_func(board: SokobanBoard, x_inc: int, y_inc: int) -> SokobanBoard:
    player_pos: Tuple = board.find_player()
    current_field: SokobanFieldType = board.get_field(*player_pos)
    field_incremented: SokobanFieldType = board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    
    if (current_field == SokobanFieldType.PLAYER_ON_GOAL):
        board.set_field(player_pos[0], player_pos[1], SokobanFieldType.GOAL)
    else:
        board.set_field(player_pos[0], player_pos[1], SokobanFieldType.AIR)
    
    if (field_incremented == SokobanFieldType.AIR):
        board.set_field(player_pos[0] + x_inc, player_pos[1] + y_inc, SokobanFieldType.PLAYER)
    else:
        board.set_field(player_pos[0] + x_inc, player_pos[1] + y_inc, SokobanFieldType.PLAYER_ON_GOAL)

    if(field_incremented == SokobanFieldType.BOX or field_incremented == SokobanFieldType.BOX_ON_GOAL):
        field_double_incremented: SokobanFieldType = board.get_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        if (field_double_incremented == SokobanFieldType.GOAL):
            board.set_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc, SokobanFieldType.BOX_ON_GOAL)
        else:
            board.set_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc, SokobanFieldType.BOX)

    return board