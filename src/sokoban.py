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

    # Special method for setting custom fields in enums
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
        self.goals: List[Tuple[int, int]] = []
        self.boxes: List[Tuple[int, int]] = []
        for x_index, row in enumerate(self.value):
            for y_index, field in enumerate(row):
                if field == SokobanFieldType.GOAL or field == SokobanFieldType.BOX_ON_GOAL or field == SokobanFieldType.PLAYER_ON_GOAL:
                    self.goals.append((x_index, y_index))
                    if field == SokobanFieldType.GOAL:
                        self.set_field(x_index, y_index, SokobanFieldType.AIR)

                if field == SokobanFieldType.PLAYER or field == SokobanFieldType.PLAYER_ON_GOAL:
                    self._player_pos: Tuple[int, int] = (x_index, y_index)
                    if field == SokobanFieldType.PLAYER_ON_GOAL:
                        self.set_field(x_index, y_index, SokobanFieldType.PLAYER)

                if field == SokobanFieldType.BOX or field == SokobanFieldType.BOX_ON_GOAL:
                    self.boxes.append((x_index, y_index))
                    if field == SokobanFieldType.BOX_ON_GOAL:
                        self.set_field(x_index, y_index, SokobanFieldType.BOX)
                    

    def is_goal(self) -> bool:
        return set(self.goals) == set(self.boxes)
    
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

    def update_box_position(self, original_position: Tuple[int, int], new_position: Tuple[int, int]):
        index = self.boxes.index(original_position) 
        self.boxes[index] = new_position
        return
    
    @property
    def player_pos(self):
        return self._player_pos

    def get_hard_copy(self):
        to_return: List[List[SokobanFieldType]] = deepcopy(self.value)
        new_board = SokobanBoard(to_return)
        new_board.goals = deepcopy(self.goals)
        return new_board
    
    def __str__(self):
        row_strings = [" ".join(field.ascii_repr.ljust(3) for field in row) for row in self.value]
        return "\n".join(row_strings)
    
    def __hash__(self):
        return hash((self._player_pos, frozenset(self.boxes)))

    def __eq__(self, other):
        return isinstance(other, SokobanBoard) and \
        self._player_pos == other._player_pos and \
        set(self.boxes) == set(other.boxes)

    



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
    player_pos = board.player_pos
    field_incremented = board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    if(field_incremented == SokobanFieldType.WALL):
        return False
    
    # If there's a box, verify that the player can actually move the box
    if(field_incremented == SokobanFieldType.BOX):
        field_double_incremented: SokobanFieldType = board.get_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        if not (field_double_incremented == SokobanFieldType.AIR):
            return False
    return True

def generic_transition_func(board: SokobanBoard, direction: SokobanDirection) -> SokobanBoard:
    x_inc, y_inc = direction.coordinates
    new_board = board.get_hard_copy()
    player_pos: Tuple = new_board.player_pos
    field_incremented: SokobanFieldType = new_board.get_field(player_pos[0] + x_inc, player_pos[1] + y_inc)
    
    new_board.set_field(player_pos[0], player_pos[1], SokobanFieldType.AIR)
    
    new_board.set_field(player_pos[0] + x_inc, player_pos[1] + y_inc, SokobanFieldType.PLAYER)

    if(field_incremented == SokobanFieldType.BOX):
        new_board.set_field(player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc, SokobanFieldType.BOX)
        new_board.update_box_position((player_pos[0] + x_inc, player_pos[1] + y_inc), (player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc))


    return new_board
