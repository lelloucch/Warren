from typing import List, Optional
from dataclasses import dataclass

# Assuming Token and Address are defined elsewhere or imported as needed
from warren_types import Token, Address, Chain, Hash

class WarrenWallet:
    # Placeholder for the WarrenWallet class
    pass

class WarrenProvider:
    # Placeholder for the WarrenProvider class
    pass

# Define the supported EVM chain list as a constant
_SUPPORTED_EVM_CHAIN_LIST = ['ethereum', 'polygon', 'binance-smart-chain']  # Example values

SupportedEVMChain = str  # String literal type
SupportedChain = str  # Union of SupportedEVMChain or 'solana'

# Transaction types
@dataclass
class Transaction:
    hash: Hash
    from_address: Address
    to: Address
    value: int
    data: Optional[str] = None
    chain_id: Optional[int] = None

# Token types
@dataclass
class TokenWithBalance:
    token: Token
    balance: int  # Use int for bigint-like values
    formatted_balance: str
    price_usd: str
    value_usd: str

@dataclass
class WalletBalance:
    chain: SupportedEVMChain
    address: Address
    total_value_usd: str
    tokens: List[TokenWithBalance]

# Chain configuration
@dataclass
class ChainMetadata:
    chain_id: int
    name: str
    chain: Chain
    rpc_url: str
    native_currency: dict
    block_explorer_url: str

@dataclass
class WarrenConfig:
    evm_private_key: Optional[str] = None  # '0x' prefixed string
    solana_private_key: Optional[str] = None
    actions: List[str]

# Base interface for all protocol parameters
@dataclass
class ActionParams:
    protocol: str
    chain: SupportedChain
    amount: str
    asset: str
    data: Optional[str] = None

@dataclass
class SupplyParams(ActionParams):
    pass

@dataclass
class WithdrawParams(ActionParams):
    pass

@dataclass
class StakeParams(ActionParams):
    pass

@dataclass
class SwapParams(ActionParams):
    contract: str
    token_in: str
    token_out: str
    amount_out: Optional[str] = None
    slippage: float
    recipient: Optional[str] = None

@dataclass
class LiquidityParams(ActionParams):
    contract: str
    token_a: str
    token_b: str
    amount_b: str

class DeFiProtocol:
    supported_chains: List[SupportedChain]

class ILendingProtocol(DeFiProtocol):
    async def supply(self, params: SupplyParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def withdraw(self, params: WithdrawParams, wallet_provider: WarrenWallet) -> Transaction:
        pass

class IStakingProtocol(DeFiProtocol):
    async def stake(self, params: StakeParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def unstake(self, params: StakeParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def claim_rewards(self, params: StakeParams, wallet_provider: WarrenWallet) -> Optional[Transaction]:
        pass

class IDEXProtocol(DeFiProtocol):
    async def swap(self, params: SwapParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def add_liquidity(self, params: LiquidityParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def remove_liquidity(self, params: LiquidityParams, wallet_provider: WarrenWallet) -> Transaction:
        pass
    
    async def get_quote(self, params: SwapParams, wallet_provider: WarrenWallet) -> Optional[str]:
        pass

@dataclass
class WarrenAction:
    name: str
    description: str
    template: str
    provider: WarrenProvider
    execute: callable  # A function that takes ActionParams and returns a Transaction
