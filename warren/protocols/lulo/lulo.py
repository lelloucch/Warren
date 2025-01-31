from typing import Dict
from web3 import Web3

class LuloProtocol:
    """Lulo Staking Protocol Integration"""

    def __init__(self, web3: Web3):
        self.web3 = web3
        self.contract = self.load_contract()

    def load_contract(self):
        """Load Lulo staking contract."""
        contract_address = "0xLuloContractAddress"  # Replace with actual Lulo contract address
        contract_abi = []  # Load ABI JSON for Lulo contract here
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def stake(self, amount: float, user_address: str) -> Dict:
        """Stake tokens into Lulo."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        tx = self.contract.functions.stake(user_address).build_transaction({
            'from': user_address,
            'value': self.web3.toWei(amount, 'ether'),  # Assuming staking in ETH, modify if it's different
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}

    def unstake(self, token_amount: float, user_address: str) -> Dict:
        """Unstake tokens from Lulo."""
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero")

        tx = self.contract.functions.unstake(token_amount).build_transaction({
            'from': user_address,
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}
