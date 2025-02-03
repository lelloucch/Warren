from typing import Dict
from web3 import Web3

class CompoundProtocol:
    """Compound Finance Integration"""

    def __init__(self, web3: Web3, contract_address: str, contract_abi: list):
        self.web3 = web3
        self.contract = self.load_contract(contract_address, contract_abi)

    def load_contract(self, contract_address: str, contract_abi: list):
        """Load the Compound cToken contract."""
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def supply(self, amount: float, user_address: str) -> Dict:
        """Supply assets to Compound (Mint cTokens)."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        tx = self.contract.functions.mint().build_transaction({
            'from': user_address,
            'value': self.web3.toWei(amount, 'ether'),  # Assuming ETH; change if using an ERC-20 token
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}

    def withdraw(self, cToken_amount: float, user_address: str) -> Dict:
        """Redeem cTokens for underlying assets."""
        if cToken_amount <= 0:
            raise ValueError("cToken amount must be greater than zero")

        tx = self.contract.functions.redeem(cToken_amount).build_transaction({
            'from': user_address,
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}
