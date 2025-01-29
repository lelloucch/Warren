from typing import Any, Dict
import logging

class Transaction:
    # Placeholder for the Transaction class
    pass

class SupplyParams:
    # Placeholder for SupplyParams
    def __init__(self, amount: float, asset: str, protocol: str, chain: str):
        self.amount = amount
        self.asset = asset
        self.protocol = protocol
        self.chain = chain

class WithdrawParams:
    # Placeholder for WithdrawParams
    def __init__(self, amount: float, asset: str, protocol: str, chain: str):
        self.amount = amount
        self.asset = asset
        self.protocol = protocol
        self.chain = chain

class EdwinProvider:
    def get_wallet(self, chain: str) -> Any:
        # Placeholder for getting wallet based on chain
        pass

class EdwinWallet:
    # Placeholder for EdwinWallet
    pass

class LendingProtocol:
    def __init__(self, supported_chains: list):
        self.supported_chains = supported_chains

    def supply(self, params: SupplyParams, wallet_provider: EdwinWallet) -> Transaction:
        # Placeholder for protocol-specific supply implementation
        pass

    def withdraw(self, params: WithdrawParams, wallet_provider: EdwinWallet) -> Transaction:
        # Placeholder for protocol-specific withdraw implementation
        pass

def get_lending_protocol(protocol_name: str) -> LendingProtocol:
    # Placeholder to get lending protocol based on the name
    pass


class SupplyAction:
    name = 'supply'
    description = 'Supply assets to a lending protocol'
    template = 'supplyTemplate'  # Placeholder for template
    provider: EdwinProvider

    def __init__(self, provider: EdwinProvider):
        self.provider = provider

    async def execute(self, params: SupplyParams) -> Transaction:
        logging.info(f"Supplying: {params.amount} {params.asset} to {params.protocol} on {params.chain}")
        try:
            logging.info(f"Getting lending protocol for: {params.protocol}")
            lending_protocol = get_lending_protocol(params.protocol)
            if not lending_protocol:
                raise ValueError(f"Unsupported protocol: {params.protocol}")
            logging.info(f"Successfully got lending protocol: {params.protocol}")

            logging.info(f"Getting wallet provider for chain: {params.chain}")
            wallet_provider = self.provider.get_wallet(params.chain)
            if not wallet_provider or not isinstance(wallet_provider, EdwinWallet):
                raise ValueError(f"Unsupported wallet provider: {params.protocol}")
            logging.info(f"Successfully got wallet provider for chain: {params.chain}")

            logging.info(f"Checking if chain {params.chain} is supported by protocol {params.protocol}")
            if params.chain not in lending_protocol.supported_chains:
                raise ValueError(f"Unsupported chain: {params.chain}")
            logging.info(f"Chain {params.chain} is supported by protocol {params.protocol}")

            logging.info(f"Executing supply operation with protocol {params.protocol}")
            return await lending_protocol.supply(params, wallet_provider)
        except Exception as error:
            raise ValueError(f"Supply failed: {str(error)}")


class WithdrawAction:
    name = 'withdraw'
    description = 'Withdraw assets from a lending protocol'
    template = 'withdrawTemplate'  # Placeholder for template
    provider: EdwinProvider

    def __init__(self, provider: EdwinProvider):
        self.provider = provider

    async def execute(self, params: WithdrawParams) -> Transaction:
        logging.info(f"Withdrawing: {params.amount} {params.asset} from {params.protocol} on {params.chain}")
        try:
            logging.info(f"Getting lending protocol for: {params.protocol}")
            lending_protocol = get_lending_protocol(params.protocol)
            if not lending_protocol:
                raise ValueError(f"Unsupported protocol: {params.protocol}")

            logging.info(f"Getting wallet provider for chain: {params.chain}")
            wallet_provider = self.provider.get_wallet(params.chain)
            if not wallet_provider:
                raise ValueError(f"Unsupported wallet provider: {params.protocol}")

            logging.info(f"Executing withdraw operation with protocol {params.protocol}")
            return await lending_protocol.withdraw(params, wallet_provider)
        except Exception as error:
            raise ValueError(f"Withdraw failed: {str(error)}")
