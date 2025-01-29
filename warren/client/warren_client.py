from typing import List, Dict, Type
from abc import ABC, abstractmethod


class WarrenProvider:
    def __init__(self, config):
        # Initialize the provider with config (example)
        self.config = config


class WarrenAction(ABC):
    def __init__(self, provider: WarrenProvider):
        self.provider = provider

    @abstractmethod
    def execute(self):
        pass


class SupplyAction(WarrenAction):
    def execute(self):
        print("Executing supply action")


class WithdrawAction(WarrenAction):
    def execute(self):
        print("Executing withdraw action")


class StakeAction(WarrenAction):
    def execute(self):
        print("Executing stake action")


ACTION_MAP: Dict[str, Type[WarrenAction]] = {
    'supply': SupplyAction,
    'withdraw': WithdrawAction,
    'stake': StakeAction
}


class Warren:
    def __init__(self, config):
        self.provider = WarrenProvider(config)
        self.actions = self._initialize_actions(config['actions'])

    def _initialize_actions(self, action_names: List[str]) -> Dict[str, WarrenAction]:
        actions = {}
        for action_name in action_names:
            ActionClass = ACTION_MAP.get(action_name)
            if not ActionClass:
                raise ValueError(f"Unsupported action: {action_name}")
            actions[action_name] = ActionClass(self.provider)
        return actions

    def get_actions(self) -> List[WarrenAction]:
        return list(self.actions.values())


# Example usage:
config = {
    'actions': ['supply', 'withdraw', 'stake']
}

warren = Warren(config)
for action in warren.get_actions():
    action.execute()
