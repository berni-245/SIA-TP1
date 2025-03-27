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
    def __init__(self, board: List[List[SokobanFieldType]], player_pos: Tuple[int, int], goals: List[Tuple[int, int]], boxes: List[Tuple[int, int]]):
        super().__init__(board)
        self.player_pos = player_pos
        self.goals = goals
        self.boxes = boxes

    @classmethod
    def board_builder(cls, board: List[List[SokobanFieldType]]):
        if not board or not all(isinstance(row, list) for row in board):
            raise ValueError("Board must be a 2D list of SokobanFieldType values")
        goals: List[Tuple[int, int]] = []
        boxes: List[Tuple[int, int]] = []
        player_pos = (0, 0)
        for x_index, row in enumerate(board):
            for y_index, field in enumerate(row):
                if field == SokobanFieldType.GOAL or field == SokobanFieldType.BOX_ON_GOAL or field == SokobanFieldType.PLAYER_ON_GOAL:
                    goals.append((x_index, y_index))

                if field == SokobanFieldType.PLAYER or field == SokobanFieldType.PLAYER_ON_GOAL:
                    player_pos: Tuple[int, int] = (x_index, y_index)

                if field == SokobanFieldType.BOX or field == SokobanFieldType.BOX_ON_GOAL:
                    boxes.append((x_index, y_index))

                if field != SokobanFieldType.WALL:
                    board[x_index][y_index] = SokobanFieldType.AIR
        return cls(board, player_pos, goals, boxes)
                    

    def is_goal(self) -> bool:
        return set(self.goals) == set(self.boxes)
    
    def get_field(self, row_index: int, col_index: int) -> SokobanFieldType:
        if not (0 <= row_index < len(self.value) and 0 <= col_index < len(self.value[row_index])):
            return SokobanFieldType.WALL

        return self.value[row_index][col_index]
    
    def update_player_pos(self, new_player_pos: Tuple[int, int]):
        self.player_pos = new_player_pos

    def update_box_position(self, original_position: Tuple[int, int], new_position: Tuple[int, int]):
        index = self.boxes.index(original_position) 
        self.boxes[index] = new_position
        return

    def get_hard_copy(self):        
        return SokobanBoard(self.value, self.player_pos, deepcopy(self.goals), deepcopy(self.boxes))

    
    def __str__(self):
        row_strings = []
        for x_idx, row in enumerate(self.value):
            formatted_row = []
            for y_idx, field in enumerate(row):              
                if ((x_idx, y_idx) in self.goals and (x_idx, y_idx) == self.player_pos):
                    formatted_row.append(SokobanFieldType.PLAYER_ON_GOAL.ascii_repr.ljust(3))    
                    continue

                if ((x_idx, y_idx) in self.goals and (x_idx, y_idx) in self.boxes):
                    formatted_row.append(SokobanFieldType.BOX_ON_GOAL.ascii_repr.ljust(3))    
                    continue

                if (x_idx, y_idx) == self.player_pos:
                    formatted_row.append(SokobanFieldType.PLAYER.ascii_repr.ljust(3))    
                elif (x_idx, y_idx) in self.boxes:
                    formatted_row.append(SokobanFieldType.BOX.ascii_repr.ljust(3))    
                elif (x_idx, y_idx) in self.goals:
                    formatted_row.append(field.ascii_repr.ljust(3))
                else:
                    formatted_row.append(field.ascii_repr.ljust(3))
            
            row_strings.append(" ".join(formatted_row))
        return "\n".join(row_strings)

    
    def __hash__(self):
        return hash((self.player_pos, frozenset(self.boxes)))

    def __eq__(self, other):
        return isinstance(other, SokobanBoard) and \
        self.player_pos == other.player_pos and \
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
    inc_player_pos = (player_pos[0] + x_inc, player_pos[1] + y_inc)
    field_incremented = board.get_field(*inc_player_pos)
    if(field_incremented == SokobanFieldType.WALL):
        return False
    
    # If there's a box, verify that the player can actually move the box
    if(inc_player_pos in board.boxes):
        double_inc_player_post = (player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        field_double_incremented: SokobanFieldType = board.get_field(*double_inc_player_post)
        if (field_double_incremented == SokobanFieldType.WALL or double_inc_player_post in board.boxes):
            return False
        
    return True

def generic_transition_func(board: SokobanBoard, direction: SokobanDirection) -> SokobanBoard:
    x_inc, y_inc = direction.coordinates
    new_board = board.get_hard_copy()
    player_pos = new_board.player_pos
    inc_player_pos = (player_pos[0] + x_inc, player_pos[1] + y_inc)

    new_board.update_player_pos(inc_player_pos)

    if(inc_player_pos in new_board.boxes):
        double_inc_player_post = (player_pos[0] + 2*x_inc, player_pos[1] + 2*y_inc)
        new_board.update_box_position(inc_player_pos, double_inc_player_post)

    return new_board
