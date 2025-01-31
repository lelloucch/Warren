from typing import Dict
from web3 import Web3

class LidoProtocol:
    """Lido Staking Protocol Integration"""

    def __init__(self, web3: Web3):
        self.web3 = web3
        self.contract = self.load_contract()

    def load_contract(self):
        """Load Lido staking contract."""
        contract_address = "0xLidoContractAddress"
        contract_abi = []  # Load ABI JSON here
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def stake(self, amount: float, user_address: str) -> Dict:
        """Stake ETH into Lido."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        tx = self.contract.functions.submit(user_address).build_transaction({
            'from': user_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}

    def unstake(self, stETH_amount: float, user_address: str) -> Dict:
        """Unstake ETH from Lido."""
        if stETH_amount <= 0:
            raise ValueError("stETH amount must be greater than zero")

        tx = self.contract.functions.requestWithdraw(stETH_amount).build_transaction({
            'from': user_address,
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })
        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}
