from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from typing import Optional, Dict


class WarrenEVMWallet:
    def __init__(self, private_key: str):
        self.current_chain = "mainnet"  # Default chain is "mainnet"
        self.chains = {}  # Will store chain configurations
        self.account = Account.from_key(private_key)  # Convert private key to account
        self.evm_private_key = private_key

    def get_address(self) -> str:
        """Return the wallet address."""
        return self.account.address

    def get_public_client(self, chain_name: str) -> Web3:
        """Return a Web3 client for the specified chain."""
        transport = self.create_http_transport(chain_name)
        return Web3(transport)

    def get_wallet_client(self, chain_name: str) -> Web3:
        """Return a wallet client for interacting with the chain."""
        transport = self.create_http_transport(chain_name)
        web3 = Web3(transport)
        web3.eth.defaultAccount = self.account.address
        return web3

    def get_chain_configs(self, chain_name: str) -> Optional[Dict]:
        """Get chain configurations from the chain name."""
        chain = self.chains.get(chain_name)
        if not chain:
            raise ValueError("Invalid chain name")
        return chain

    def get_wallet_balance(self) -> Optional[str]:
        """Get the balance of the wallet for the current chain."""
        try:
            client = self.get_public_client(self.current_chain)
            balance = client.eth.get_balance(self.account.address)
            return Web3.fromWei(balance, 'ether')  # Convert from wei to ether
        except Exception as e:
            print(f"Error getting wallet balance: {e}")
            return None

    def get_wallet_balance_for_chain(self, chain_name: str) -> Optional[str]:
        """Get the balance of the wallet for a specific chain."""
        try:
            client = self.get_public_client(chain_name)
            balance = client.eth.get_balance(self.account.address)
            return Web3.fromWei(balance, 'ether')  # Convert from wei to ether
        except Exception as e:
            print(f"Error getting wallet balance: {e}")
            return None

    def add_chain(self, chain: Dict[str, Dict]):
        """Add a new chain configuration."""
        self.set_chains(chain)

    def switch_chain(self, chain_name: str, custom_rpc_url: Optional[str] = None):
        """Switch to a different blockchain."""
        if chain_name not in self.chains:
            chain = self.gen_chain_from_name(chain_name, custom_rpc_url)
            self.add_chain({chain_name: chain})
        self.set_current_chain(chain_name)

    def set_account(self, private_key: str):
        """Set the account using a new private key."""
        self.account = Account.from_key(private_key)

    def set_chains(self, chains: Optional[Dict[str, Dict]] = None):
        """Set the chains' configurations."""
        if chains:
            self.chains.update(chains)

    def set_current_chain(self, chain_name: str):
        """Set the current chain to interact with."""
        self.current_chain = chain_name

    def create_http_transport(self, chain_name: str):
        """Create HTTP transport for interacting with a blockchain."""
        # For simplicity, let's assume each chain has a custom RPC URL
        chain = self.chains.get(chain_name)
        if not chain:
            raise ValueError("Chain not found")
        custom_rpc_url = chain.get('rpcUrl', 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')
        web3 = Web3(Web3.HTTPProvider(custom_rpc_url))
        if chain_name == "ropsten":
            web3.middleware_stack.inject(geth_poa_middleware, layer=0)
        return web3

    @staticmethod
    def gen_chain_from_name(chain_name: str, custom_rpc_url: Optional[str] = None) -> Dict:
        """Generate chain configuration based on the name."""
        base_chain = {
            'mainnet': {
                'rpcUrl': 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
            },
            'ropsten': {
                'rpcUrl': 'https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID'
            }
            # Add more chain configurations as needed
        }

        if chain_name not in base_chain:
            raise ValueError("Invalid chain name")

        chain_config = base_chain[chain_name]
        if custom_rpc_url:
            chain_config['rpcUrl'] = custom_rpc_url
        return chain_config


# Example usage:
private_key = "0xYOUR_PRIVATE_KEY"
wallet = WarrenEVMWallet(private_key)
print(f"Wallet address: {wallet.get_address()}")
balance = wallet.get_wallet_balance()
print(f"Wallet balance: {balance} ETH")
