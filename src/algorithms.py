from anytree import Node
from typing import List, Tuple, Callable
from state import State, Action

def search_algorithm(
        initial_state: State, goals: List[State], actions: List[Action], sort_frontier_function: Callable[[Node], int]
) -> Tuple[Node]:
    frontier: List[Node] = []
    root_node = Node(initial_state)
    frontier.append(root_node)
    visited: set[State] = set()

    while len(frontier) > 0:
        current_node: Node = frontier.pop(0)
        current_state: State = current_node.name

        visited.add(current_state)

        if current_state in goals:
            return current_node.path
        for action in actions:
            if action.can_execute(current_state):
                new_state = action.execute(current_state)
                if new_state in visited:
                    continue
                new_node = Node(new_state, parent=current_node)
                frontier.append(new_node)

        frontier.sort(key=sort_frontier_function)

    return ()

def bfs(node: Node):
    return len(node.path)

def dfs(node: Node):
    return node.root.height + 1 - len(node.path)