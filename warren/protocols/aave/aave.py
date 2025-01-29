from web3 import Web3
from typing import List, Dict, Any

class AaveProtocol:
    supported_chains = ["base"]

    def get_aave_chain(self, chain: str) -> str:
        if chain not in self.supported_chains:
            raise ValueError(f"Chain {chain} is not supported by Aave protocol")
        return chain

    def submit_transaction(self, web3: Web3, wallet, tx: Dict[str, Any]) -> Any:
        try:
            signed_tx = wallet.sign_transaction(tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as error:
            raise RuntimeError(f"Transaction failed: {str(error)}")

    def supply(self, params: Dict[str, Any], wallet_provider) -> Dict[str, Any]:
        chain, amount, asset = params["chain"], params["amount"], params["asset"]
        print(f"Calling the inner AAVE logic to supply {amount} {asset}")

        try:
            aave_chain = self.get_aave_chain(chain)
            wallet_provider.switch_chain(aave_chain)
            wallet_client = wallet_provider.get_wallet_client(aave_chain)
            print(f"Switched to chain: {chain}")

            web3 = Web3(Web3.HTTPProvider(wallet_client.transport.url))
            wallet = wallet_provider.get_web3_wallet(wallet_client, web3)
            
            # Example: Fetch user balance
            balance = web3.eth.get_balance(wallet.address)
            print(f"Balance: {balance}")
            
            # Prepare transaction (Placeholder, should be replaced with Aave contract call)
            tx = {
                "to": "AAVE_POOL_ADDRESS",  # Replace with actual Aave Pool contract address
                "value": Web3.to_wei(amount, "ether"),
                "gas": 200000,
                "gasPrice": web3.eth.gas_price,
                "nonce": web3.eth.get_transaction_count(wallet.address),
            }
            
            tx_receipt = self.submit_transaction(web3, wallet, tx)
            return {
                "hash": tx_receipt.transactionHash.hex(),
                "from": tx_receipt['from'],
                "to": tx_receipt['to'],
                "value": amount,
            }
        except Exception as error:
            print(f"Aave supply error: {error}")
            raise RuntimeError(f"Aave supply failed: {str(error)}")

    def withdraw(self, params: Dict[str, Any], wallet_provider) -> Dict[str, Any]:
        print(f"Calling the inner AAVE logic to withdraw {params['amount']} {params['asset']}")
        raise NotImplementedError("Withdraw function is not implemented yet")
