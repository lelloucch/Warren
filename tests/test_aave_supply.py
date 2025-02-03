import os
import pytest
from dotenv import load_dotenv
from warren import Warren, WarrenConfig

# Load environment variables
load_dotenv()


def test_edwin_aave():
    evm_private_key = os.getenv("EVM_PRIVATE_KEY")
    if not evm_private_key:
        pytest.fail("EVM_PRIVATE_KEY is not set")

    edwin_config = WarrenConfig(
        evm_private_key=evm_private_key,
        actions=["supply"]
    )

    warren = Warren(edwin_config)
    assert warren is not None

    # Test supply action
    result = warren.actions.supply.execute({
        "protocol": "aave",
        "chain": "base",
        "amount": "0.05",
        "asset": "usdc"
    })

    assert result is not None
    assert result["hash"].startswith("0x")
    assert result["from"].startswith("0x")
    assert result["to"].startswith("0x")
    assert result["value"] == 0.05
