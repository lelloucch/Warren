from typing import Dict
from web3 import Web3

class AaveProtocol:
    """Aave Lending Protocol Integration"""

    def __init__(self, web3: Web3):
        self.web3 = web3
        self.contract = self.load_contract()

    def load_contract(self):
        """Load Aave lending contract."""
        # Replace with actual contract ABI and address
        contract_address = "0xAaveContractAddress"
        contract_abi = []  # Load ABI JSON here
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def supply(self, asset: str, amount: float, user_address: str) -> Dict:
        """Supplies assets to Aave Lending Pool."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        tx = self.contract.functions.deposit(asset, amount, user_address, 0).build_transaction({
            'from': user_address,
            'gas': 500000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}

    def withdraw(self, asset: str, amount: float, user_address: str) -> Dict:
        """Withdraws supplied assets from Aave Lending Pool."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        tx = self.contract.functions.withdraw(asset, amount, user_address).build_transaction({
            'from': user_address,
            'gas': 500000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}
