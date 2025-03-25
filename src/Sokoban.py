from state import State, Action
from enum import Enum
from typing import List, Tuple
from copy import deepcopy

class SokobanFieldType(Enum):
    AIR = ("Air", "_")
    WALL = ("Wall", "#")
    PLAYER = ("Player", "O")
    BOX = ("Box", "[]")
    GOAL = ("Goal", "{}")
    PLAYER_ON_GOAL = ("Player On Goal", "{O}")
    BOX_ON_GOAL = ("Box On Goal", "{[]}")

    def __init__(self, label: str, ascii_repr: str):
        self._label = label
        self._ascii_repr = ascii_repr

    @property
    def ascii_repr(self):
        return self._ascii_repr

class SokobanAction(Action, Enum):
    UP = (
        "Up action",
        lambda board: generic_transition_func(board, SokobanDirection.UP), 
        lambda board: generic_can_run_action(board, SokobanDirection.UP),
        1
    )
    DOWN = (
        "Down action",
        lambda board: generic_transition_func(board, SokobanDirection.DOWN), 
        lambda board: generic_can_run_action(board, SokobanDirection.DOWN),
        1
    )
    LEFT = (
        "Left action",
        lambda board: generic_transition_func(board, SokobanDirection.LEFT), 
        lambda board: generic_can_run_action(board, SokobanDirection.LEFT),
        1
    )
    RIGHT = (
        "Right action",
        lambda board: generic_transition_func(board, SokobanDirection.RIGHT), 
        lambda board: generic_can_run_action(board, SokobanDirection.RIGHT),
        1
    )

    def __new__(cls, action_name, action, can_do_action, cost):
        obj = object.__new__(cls)
        obj._action_name = action_name
        obj._action = action
        obj._can_do_action = can_do_action
        obj._cost = cost
        return obj
    
    def __str__(self):
        return self._action_name
    
class SokobanBoard(State):
    def __init__(self, board: List[List[SokobanFieldType]]):
        if not board or not all(isinstance(row, list) for row in board):
            raise ValueError("Board must be a 2D list of SokobanFieldType values")
        super().__init__(board)
        self._player_pos: Tuple[int, int] = self._find_player()
    
    def get_field(self, row_index: int, col_index: int) -> SokobanFieldType:
        if not (0 <= row_index < len(self.value) and 0 <= col_index < len(self.value[row_index])):
            return SokobanFieldType.WALL

        return self.value[row_index][col_index]
    
    def set_field(self, row_index: int, col_index: int, field: SokobanFieldType) -> None:
        if not (0 <= row_index < len(self.value) and 0 <= col_index < len(self.value[row_index])):
            raise IndexError("Field position is out of bounds")

        if (field == SokobanFieldType.PLAYER or field == SokobanFieldType.PLAYER_ON_GOAL):
            self._player_pos = (row_index, col_index)
        self.value[row_index][col_index] = field
    
    @property
    def player_pos(self):
        return self._player_pos
    
    def get_hard_copy(self):
        to_return: List[List[SokobanFieldType]] = deepcopy(self.value)
        return SokobanBoard(to_return)
    
    def _find_player(self) -> Tuple[int, int]:
        for row_index, row in enumerate(self.value):
            for col_index, field in enumerate(row):
                if field == SokobanFieldType.PLAYER or field == SokobanFieldType.PLAYER_ON_GOAL:
                    return (row_index, col_index)
        raise ValueError("No player was found")
    
    def __str__(self):
        row_strings = [" ".join(field.ascii_repr.ljust(3) for field in row) for row in self.value]
        return "\n".join(row_strings)


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
            raise RuntimeError("There's no more boards available")
        self._index += 1
        self._current_board = self._boards_list[self._index]
        return self


    def execute_action(self, action: SokobanAction):
        if (action.can_execute(self._current_board)):
            self._current_board = action.execute(self._current_board)
        return self
        
    def get_board(self):
        return self._current_board
    
    def set_current_board(self, new_board: SokobanBoard):
        self._current_board = new_board
        return self
    
class SokobanDirection(Enum):
    UP = (-1, 0)  
    DOWN = (1, 0)  
    LEFT = (0, -1)  
    RIGHT = (0, 1)  

    @property
    def coordinates(self):
        return self.value

def generic_can_run_action(board: SokobanBoard, direction: SokobanDirection) -> bool:
    x_inc, y_inc = direction.coordinates
    player_pos: Tuple = board.player_pos
    field_incremented: SokobanFieldType = board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    if(field_incremented == SokobanFieldType.WALL):
        return False
    
    # If there's a box, verify that the player can actually move the box
    if(field_incremented == SokobanFieldType.BOX or field_incremented == SokobanFieldType.BOX_ON_GOAL):
        field_double_incremented: SokobanFieldType = board.get_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        if not (field_double_incremented == SokobanFieldType.AIR or field_double_incremented == SokobanFieldType.GOAL):
            return False
    return True

def generic_transition_func(board: SokobanBoard, direction: SokobanDirection) -> SokobanBoard:
    x_inc, y_inc = direction.coordinates
    new_board = board.get_hard_copy()
    player_pos: Tuple = new_board.player_pos
    current_field: SokobanFieldType = new_board.get_field(*player_pos)
    field_incremented: SokobanFieldType = new_board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    
    if (current_field == SokobanFieldType.PLAYER_ON_GOAL):
        new_board.set_field(player_pos[0], player_pos[1], SokobanFieldType.GOAL)
    else:
        new_board.set_field(player_pos[0], player_pos[1], SokobanFieldType.AIR)
    
    if not (field_incremented == SokobanFieldType.GOAL or field_incremented == SokobanFieldType.BOX_ON_GOAL):
        new_board.set_field(player_pos[0] + x_inc, player_pos[1] + y_inc, SokobanFieldType.PLAYER)
    else:
        new_board.set_field(player_pos[0] + x_inc, player_pos[1] + y_inc, SokobanFieldType.PLAYER_ON_GOAL)

    if(field_incremented == SokobanFieldType.BOX or field_incremented == SokobanFieldType.BOX_ON_GOAL):
        field_double_incremented: SokobanFieldType = new_board.get_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        if (field_double_incremented == SokobanFieldType.GOAL):
            new_board.set_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc, SokobanFieldType.BOX_ON_GOAL)
        else:
            new_board.set_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc, SokobanFieldType.BOX)

    return new_board