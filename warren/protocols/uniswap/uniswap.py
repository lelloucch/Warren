from typing import Dict
from web3 import Web3

class UniswapProtocol:
    """Uniswap Swap and Liquidity Management"""

    def __init__(self, web3: Web3, router_address: str, router_abi: list):
        self.web3 = web3
        self.router = self.load_router(router_address, router_abi)

    def load_router(self, router_address: str, router_abi: list):
        """Load Uniswap Router Contract."""
        return self.web3.eth.contract(address=router_address, abi=router_abi)

    def swap_tokens(self, amount_in: float, token_in: str, token_out: str, user_address: str) -> Dict:
        """Swap one token for another."""
        if amount_in <= 0:
            raise ValueError("Amount must be greater than zero")

        path = [token_in, token_out]  # Token swap path
        deadline = self.web3.eth.getBlock('latest')['timestamp'] + 600  # 10 min deadline

        tx = self.router.functions.swapExactTokensForTokens(
            self.web3.toWei(amount_in, 'ether'),
            0,  # Minimum output (should be set dynamically)
            path,
            user_address,
            deadline
        ).build_transaction({
            'from': user_address,
            'gas': 200000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })

        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}

    def add_liquidity(self, token_a: str, token_b: str, amount_a: float, amount_b: float, user_address: str) -> Dict:
        """Add liquidity to Uniswap."""
        if amount_a <= 0 or amount_b <= 0:
            raise ValueError("Amounts must be greater than zero")

        tx = self.router.functions.addLiquidity(
            token_a,
            token_b,
            self.web3.toWei(amount_a, 'ether'),
            self.web3.toWei(amount_b, 'ether'),
            0,  # Min amount A (should be set dynamically)
            0,  # Min amount B
            user_address,
            self.web3.eth.getBlock('latest')['timestamp'] + 600  # 10 min deadline
        ).build_transaction({
            'from': user_address,
            'gas': 300000,
            'gasPrice': self.web3.toWei('5', 'gwei')
        })

        tx_hash = self.web3.eth.send_transaction(tx)
        return {"tx_hash": tx_hash.hex(), "status": "pending"}
