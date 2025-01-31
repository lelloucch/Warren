# Architecture Documentation for Warren DeFAI SDK

## Overview
Warren is a Python-based SDK designed to enable AI agents to interact with decentralized finance (DeFi) protocols. It provides a unified interface for operations such as lending, staking, and decentralized exchange (DEX) trading across multiple blockchain platforms.

## System Components

### 1. **Core Modules**
- **Lending Protocols**: Provides an abstraction for DeFi lending platforms like Aave and Lulo.
- **Staking Protocols**: Manages staking interactions with platforms like Lido.
- **DEX Protocols**: Facilitates token swaps through decentralized exchanges.

### 2. **Protocol Factory**
The protocol factory pattern is used to dynamically instantiate protocol handlers based on user input. It includes:
- `get_lending_protocol(name: str)`: Returns an instance of the requested lending protocol.
- `get_staking_protocol(name: str)`: Returns an instance of the requested staking protocol.
- `get_dex_protocol(name: str)`: Returns an instance of the requested DEX protocol.

### 3. **Blockchain Interaction Layer**
This layer ensures secure interaction with different blockchain networks. It includes:
- **Wallet Integration**: Supports private key-based authentication for Ethereum and Solana wallets.
- **Transaction Handling**: Signs and submits blockchain transactions.
- **API Communication**: Fetches transaction metadata from external services (e.g., FlexLend API).

### 4. **Configuration Management**
The SDK utilizes environment variables to manage sensitive credentials:
- `EVM_PRIVATE_KEY`: Private key for Ethereum-based interactions.
- `SOLANA_PRIVATE_KEY`: Private key for Solana-based interactions.
- `FLEXLEND_API_KEY`: API key for interacting with Lulo's lending services.

## System Workflow
### 1. **Supply Tokens to a Lending Protocol**
1. User initializes the SDK with configuration parameters.
2. `get_lending_protocol(name)` is called to instantiate the appropriate protocol handler.
3. The handler calls the external API (e.g., Lulo) to generate a transaction.
4. The transaction is signed and sent to the blockchain network.
5. A response containing the transaction hash is returned.

### 2. **Withdraw Funds from a Lending Protocol**
1. The user requests a withdrawal operation.
2. The protocol handler fetches the withdrawal transaction data from the lending platform.
3. The transaction is signed and submitted to the blockchain.
4. The user receives a confirmation and transaction details.

### 3. **Token Swaps on a DEX**
1. The user calls `get_dex_protocol(name)` to get the correct DEX handler.
2. The handler constructs a swap transaction.
3. The transaction is signed and executed on the blockchain.
4. A transaction receipt is returned.

## Security Considerations
- **Private Key Management**: Ensures that private keys are never exposed in logs or API calls.
- **Rate Limiting**: API calls are optimized to prevent excessive requests.
- **Transaction Validation**: Ensures proper input validation before sending transactions.

## Future Enhancements
- Support for additional lending protocols like Compound.
- Integration with more DEX platforms.
- Enhanced AI-driven decision-making for DeFi interactions.

---
This document provides a comprehensive overview of the Warren SDK's architecture and workflow. For further details, refer to the API documentation.

