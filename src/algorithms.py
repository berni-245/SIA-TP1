from math import sqrt
from anytree import Node
from typing import Sequence, Tuple, Callable

from sokoban import SokobanBoard, SokobanFieldType as SF
from state import State, Action
from sortedcontainers import SortedList
import numpy as np

def search_algorithm(
        initial_state: State, actions: Sequence[Action], sort_frontier_function: Callable[[Node], int]
) -> Tuple[Node, ...]:
    # frontier: List[Node] = []
    frontier: SortedList = SortedList(key=sort_frontier_function)
    root_node = Node(initial_state)
    frontier.add(root_node)
    visited: set[State] = set()

    while len(frontier) > 0:
        current_node: Node = frontier.pop(0)
        current_state: State = current_node.name

        visited.add(current_state)

        if current_state.is_goal():
            return current_node.path
        for action in actions:
            if action.can_execute(current_state):
                new_state = action.execute(current_state)
                if new_state in visited:
                    continue
                new_node = Node(new_state, parent=current_node)
                frontier.add(new_node)

    return ()


def bfs(node: Node):
    return len(node.path)


def dfs(node: Node):
    return node.root.height + 1 - len(node.path)

def greedy(node: Node):
    return heuristic_man_no_corners(node.name)

def heuristic_manhatan(board: SokobanBoard) -> int:
    tot = 0
    boxes = board.boxes.copy()
    (px, py) = board.player_pos
    dists = np.empty(len(board.boxes))
    for (gx, gy) in board.goals:
        goal_already_full = False
        for i, (bx, by) in enumerate(boxes):
            g_to_b_dist = abs(bx - gx) + abs(by - gy)
            if g_to_b_dist == 0:
                goal_already_full = True
                boxes.pop(i)
                dists.resize(dists.shape[0] - 1, refcheck=False)
                break
            else:
                dist = abs(px - bx) + abs(py - by) + abs(bx - gx) + abs(by - gy)
                dists[i] = dist

        if goal_already_full:
            continue

        closest_idx = np.argmin(dists)
        tot += dists[closest_idx]
        boxes.pop(closest_idx)
        dists.resize(dists.shape[0] - 1, refcheck=False)

    return tot

def heuristic_euclidean(board: SokobanBoard) -> int:
    tot = 0
    boxes = board.boxes.copy()
    (px, py) = board.player_pos
    dists = np.empty(len(board.boxes))
    for (gx, gy) in board.goals:
        goal_already_full = False
        for i, (bx, by) in enumerate(boxes):
            g_to_b_dist = abs(bx - gx) + abs(by - gy)
            if g_to_b_dist == 0:
                goal_already_full = True
                boxes.pop(i)
                dists.resize(dists.shape[0] - 1, refcheck=False)
                break
            else:
                dist = sqrt((abs(px - bx) + abs(py - by))**2 + (abs(bx - gx) + abs(by - gy))**2)
                dists[i] = dist

        if goal_already_full:
            continue

        closest_idx = np.argmin(dists)
        tot += dists[closest_idx]
        boxes.pop(closest_idx)
        dists.resize(dists.shape[0] - 1, refcheck=False)

    return tot

large_value = 99999
def heuristic_man_no_corners(board: SokobanBoard) -> int:
    for (br, bc) in board.boxes:
        up_field = board.get_field(br - 1, bc)
        down_field = board.get_field(br + 1, bc)
        left_field = board.get_field(br, bc - 1)
        right_field = board.get_field(br, bc + 1)
        # print('up', up_field)
        # print('down', down_field)
        # print('left', left_field)
        # print('right', right_field)
        if  up_field == SF.WALL and (left_field == SF.WALL or right_field == SF.WALL):
            return large_value
        elif  down_field == SF.WALL and (left_field == SF.WALL or right_field == SF.WALL):
            return large_value

    return heuristic_manhatan(board)


def heuristic_no_dead(board: SokobanBoard) -> int:
    for (br, bc) in board.boxes:
        up_field = board.get_field(br - 1, bc)
        down_field = board.get_field(br + 1, bc)
        left_field = board.get_field(br, bc - 1)
        right_field = board.get_field(br, bc + 1)
        # print('up', up_field)
        # print('down', down_field)
        # print('left', left_field)
        # print('right', right_field)
        if  up_field == SF.WALL and (left_field == SF.WALL or right_field == SF.WALL):
            return large_value
        elif  down_field == SF.WALL and (left_field == SF.WALL or right_field == SF.WALL):
            return large_value

        wall_lim_0: int
        wall_lim_1: int
        is_valid: bool = True
        if up_field == SF.WALL or down_field == SF.WALL:
            is_valid = False
            col = bc
            while True:
                col -= 1
                field = board.get_field(br, col)
                if field == SF.WALL:
                    wall_lim_0 = col
                    break
                elif field == SF.GOAL:
                    is_valid = True
            if not is_valid:
                col = bc
                while True:
                    col += 1
                    field = board.get_field(br, col)
                    if field == SF.WALL:
                        wall_lim_1 = col
                        break
                    elif field == SF.GOAL:
                        is_valid = True
                # print('lims: ', wall_lim_0, wall_lim_1)
                # print('valid: ', is_valid)
                if not is_valid:
                    dy = -1 if up_field == SF.WALL else 1
                    # print('dy', dy)
                    for col in range(wall_lim_0 + 1, wall_lim_1 - 1):
                        field = board.get_field(br + dy, col)
                        if field != SF.WALL:
                            is_valid = True
                            break
        if left_field == SF.WALL or right_field == SF.WALL:
            is_valid = False
            col = br
            while True:
                col -= 1
                field = board.get_field(col, bc)
                if field == SF.WALL:
                    wall_lim_0 = col
                    break
                elif field == SF.GOAL:
                    is_valid = True
            if not is_valid:
                col = br
                while True:
                    col += 1
                    field = board.get_field(col, bc)
                    if field == SF.WALL:
                        wall_lim_1 = col
                        break
                    elif field == SF.GOAL:
                        is_valid = True
                if not is_valid:
                    dy = -1 if left_field == SF.WALL else 1
                    for row in range(wall_lim_0 + 1, wall_lim_1 - 1):
                        field = board.get_field(row, bc + dy)
                        if field != SF.WALL:
                            is_valid = True
                            break
        # print(is_valid)
        if not is_valid:
            return large_value

    return heuristic_manhatan(board)

def a_star(node: Node):
    return len(node.path) - 1 + heuristic_euclidean(node.name)
