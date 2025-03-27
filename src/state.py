from collections.abc import Callable
from typing import Any
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, value: Any):
        self.value = value

    @abstractmethod
    def is_goal(self) -> bool:
        pass

    def __str__(self):
        return str(self.value)
    
    def __hash__(self):
        raise NotImplementedError("The class inherited from State must implement __hash__")


    def __eq__(self, other):
        raise NotImplementedError("The class inherited from State must implement __eq__")

class Action:
    def __init__(self, action_name: str, action: Callable[[State], State], can_do_action: Callable[[State], bool], cost: int):
        self._action_name = action_name
        self._action = action
        self._can_do_action = can_do_action
        self._cost = cost

    def can_execute(self, current_state: State) -> bool:
        return self._can_do_action(current_state)
    
    def execute(self, current_state: State) -> State:
        if not self.can_execute(current_state):
            raise RuntimeError('Cannot execute action')
        return self._action(current_state)

    def __str__(self):
        return self._action_name
