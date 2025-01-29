from typing import List, Dict, Any
from abc import ABC, abstractmethod

class IStakingProtocol(ABC):
    @abstractmethod
    def stake(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def unstake(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def claim_rewards(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        pass

class LidoProtocol(IStakingProtocol):
    supported_chains: List[str] = ["mainnet"]

    def stake(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        chain = params.get("chain")
        amount = params.get("amount")
        raise NotImplementedError("Stake method not implemented")

    def unstake(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        chain = params.get("chain")
        amount = params.get("amount")
        raise NotImplementedError("Unstake method not implemented")

    def claim_rewards(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        chain = params.get("chain")
        raise NotImplementedError("Claim rewards method not implemented")
