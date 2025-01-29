import base58
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana import system_program

class WarrenSolanaWallet:
    def __init__(self, private_key: str):
        # Decode the private key from base58 and create a Keypair
        decoded_key = base58.b58decode(private_key)
        self.wallet = Keypair.from_secret_key(decoded_key)
        self.wallet_address = self.wallet.public_key

    def get_public_key(self) -> PublicKey:
        """Return the public key of the wallet."""
        return self.wallet_address

    def get_connection(self, custom_rpc_url: str = None) -> Client:
        """Return a connection to the Solana blockchain."""
        rpc_url = custom_rpc_url or "https://api.mainnet-beta.solana.com"
        return Client(rpc_url)

    def sign_transaction(self, transaction: Transaction):
        """Sign a transaction using the wallet's private key."""
        transaction.sign(self.wallet)

    def get_address(self) -> str:
        """Return the wallet address (Base58 encoding)."""
        return str(self.wallet_address)

    def get_signer(self) -> Keypair:
        """Return the Keypair used for signing transactions."""
        return self.wallet


# Example usage:
private_key = "your_base58_encoded_private_key_here"
wallet = WarrenSolanaWallet(private_key)

# Get the wallet's public address
print(f"Wallet address: {wallet.get_address()}")

# Create a connection to the Solana network
connection = wallet.get_connection()

# Example of signing a transaction
transaction = Transaction()
# Add instructions to the transaction (you would normally add something here)
transaction.add(system_program.transfer(
    from_pubkey=wallet.get_public_key(),
    to_pubkey=PublicKey("RecipientAddressHere"),
    lamports=1000
))

wallet.sign_transaction(transaction)

# Print the signed transaction
print(f"Signed Transaction: {transaction}")
