from typing import Callable

class State:
    def __init__(self, value: any):
        self._value = value
        self.accumulated_cost = 0

    def __repr__(self):
        return self.value.__repr__()
    
    @property
    def value(self):
        return self._value
    
    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, State) and self._value == other._value
    
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

    def __repr__(self):
        return self._action_name