import os
import requests
from typing import Dict, Any, List
from abc import ABC, abstractmethod
from solana.transaction import Transaction as SolanaTransaction
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TxOpts

class ILendingProtocol(ABC):
    @abstractmethod
    def supply(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def withdraw(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        pass

class LuloProtocol(ILendingProtocol):
    supported_chains: List[str] = ["solana"]

    def supply(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        try:
            if not os.getenv("FLEXLEND_API_KEY"):
                raise ValueError("FLEXLEND_API_KEY is not set (For lulo.fi)")

            response = requests.post(
                "https://api.flexlend.fi/generate/account/deposit?priorityFee=50000",
                headers={
                    "Content-Type": "application/json",
                    "x-wallet-pubkey": wallet_provider.get_public_key(),
                    "x-api-key": os.getenv("FLEXLEND_API_KEY"),
                },
                json={
                    "owner": wallet_provider.get_public_key(),
                    "mintAddress": params["asset"],
                    "depositAmount": str(params["amount"]),
                },
            )
            
            response.raise_for_status()
            data = response.json()
            transaction_meta = data["data"]["transactionMeta"][0]
            
            connection = wallet_provider.get_connection()
            blockhash = connection.get_latest_blockhash()
            
            transaction = SolanaTransaction.deserialize(transaction_meta["transaction"].encode("base64"))
            transaction.recent_blockhash = blockhash
            
            wallet_provider.sign_transaction(transaction)
            signature = connection.send_transaction(transaction, opts=TxOpts(preflight_commitment="confirmed", max_retries=3))
            
            latest_blockhash = connection.get_latest_blockhash()
            connection.confirm_transaction(signature, commitment="confirmed")
            
            return {
                "hash": signature,
                "from": wallet_provider.get_public_key(),
                "to": transaction_meta["to"],
                "value": float(params["amount"]),
            }
        except Exception as error:
            raise ValueError(f"Lulo supply failed: {str(error)}")

    def withdraw(self, params: Dict[str, Any], wallet_provider: Any) -> Dict[str, Any]:
        try:
            response = requests.post(
                f"https://blink.lulo.fi/actions/withdraw?amount={params['amount']}&symbol={params['asset']}",
                headers={"Content-Type": "application/json"},
                json={"account": wallet_provider.get_public_key()},
            )
            
            response.raise_for_status()
            data = response.json()
            transaction = SolanaTransaction.deserialize(data["transaction"].encode("base64"))
            
            return {
                "hash": data["signature"],
                "from": wallet_provider.get_public_key(),
                "to": data["to"],
                "value": float(params["amount"]),
            }
        except Exception as error:
            raise ValueError(f"Lulo withdraw failed: {str(error)}")