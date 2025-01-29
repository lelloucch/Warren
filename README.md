# Warren

Warren is a Python library that bridges AI agents and DeFi protocols. It offers a unified and secure interface for AI agents to interact with various DeFi protocols while abstracting the complexities of blockchain operations and protocol-specific implementations. This empowers the creation of sophisticated DeFAI agents.

## Installation

```bash
pip install warren-sdk
```

## Features

- Lending/Borrowing operations
- Liquidity provision
- Cross-chain support
- Type-safe protocol interactions
- AI-friendly templates

## Quick Start

```python
from warren_sdk import Warren, WarrenConfig

# Configure Warren wallets and providers
warren_config = WarrenConfig(
    evm_private_key="your-evm-private-key",
    solana_private_key="your-solana-private-key",
    actions=['supply', 'withdraw', 'stake']
)

# Initialize Warren SDK
warren = Warren(warren_config)

# Supply tokens to a lending protocol
await warren.actions.supply.execute(
    protocol='aave',
    chain='base',
    amount='100',
    asset='usdc'
)
```

## Documentation

For detailed documentation, visit [docs.warren.finance](https://docs.warren.finance)

## Contributing

Contributions are welcome! Please visit our [Contributing Guide](https://docs.warren.finance) for details.

## License

MIT

---

Let me know if you'd like any adjustments!
