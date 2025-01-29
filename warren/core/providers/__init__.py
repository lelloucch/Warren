from typing import Dict
from .evm_wallet import WarrenEVMWallet, _SupportedEVMChainList
from .solana_wallet import WarrenSolanaWallet
from .wallet import WarrenWallet
from ...warren_types import WarrenConfig, SupportedChain

class WarrenProvider:
    def __init__(self, config: WarrenConfig):
        self.wallets: Dict[str, WarrenWallet] = {}

        if config.get('evmPrivateKey'):
            self.wallets['evm'] = WarrenEVMWallet(config['evmPrivateKey'])

        if config.get('solanaPrivateKey'):
            self.wallets['solana'] = WarrenSolanaWallet(config['solanaPrivateKey'])

    def get_wallet(self, chain: SupportedChain) -> WarrenWallet:
        # Check if the chain is an EVM chain using the list from evm_wallet
        evm_chain_names = [name.lower() for name in _SupportedEVMChainList]
        
        if chain.lower() in evm_chain_names:
            return self.wallets['evm']
        elif chain.lower() == 'solana':
            return self.wallets['solana']
        
        raise ValueError(f"No matching wallet is loaded in Warren to support chain: {chain}")

# Export the classes if needed
from .wallet import WarrenWallet
from .evm_wallet import WarrenEVMWallet
