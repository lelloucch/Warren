import pytest
from web3 import Web3
from unittest.mock import MagicMock
from ..warren.protocols import LidoProtocol


def test_lido_stake():
    web3 = MagicMock(spec=Web3)
    web3.toWei = Web3.toWei
    web3.eth.contract.return_value.functions.submit.return_value\
        .build_transaction.return_value = {
            'from': '0xUserAddress',
            'value': Web3.toWei(0.1, 'ether'),
            'gas': 200000,
            'gasPrice': Web3.toWei('5', 'gwei')
        }
    web3.eth.send_transaction.return_value.hex.return_value = "0xFakeTxHash"

    lido = LidoProtocol(web3)
    result = lido.stake(0.1, "0xUserAddress")

    assert result["tx_hash"] == "0xFakeTxHash"
    assert result["status"] == "pending"


def test_lido_unstake():
    web3 = MagicMock(spec=Web3)
    web3.toWei = Web3.toWei
    web3.eth.contract.return_value.functions.requestWithdraw.return_value\
        .build_transaction.return_value = {
            'from': '0xUserAddress',
            'gas': 200000,
            'gasPrice': Web3.toWei('5', 'gwei')
        }
    web3.eth.send_transaction.return_value.hex.return_value = "0xFakeTxHash"

    lido = LidoProtocol(web3)
    result = lido.unstake(0.1, "0xUserAddress")

    assert result["tx_hash"] == "0xFakeTxHash"
    assert result["status"] == "pending"


def test_lido_invalid_stake():
    web3 = MagicMock(spec=Web3)
    lido = LidoProtocol(web3)

    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        lido.stake(0, "0xUserAddress")


def test_lido_invalid_unstake():
    web3 = MagicMock(spec=Web3)
    lido = LidoProtocol(web3)

    with pytest.raises(ValueError, match="stETH amount must be greater than zero"):
        lido.unstake(0, "0xUserAddress")
