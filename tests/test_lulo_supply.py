import pytest
from web3 import Web3
from unittest.mock import MagicMock
from ..warren.protocols import LuloProtocol  

def test_lulo_stake():
    web3 = MagicMock(spec=Web3)
    web3.toWei = Web3.toWei 
    web3.eth.contract.return_value.functions.stake.return_value.build_transaction.return_value = {
        'from': '0xUserAddress',
        'value': Web3.toWei(0.1, 'ether'),
        'gas': 200000,
        'gasPrice': Web3.toWei('5', 'gwei')
    }
    web3.eth.send_transaction.return_value.hex.return_value = "0xFakeTxHash"
    
    lulo = LuloProtocol(web3)
    result = lulo.stake(0.1, "0xUserAddress")
    
    assert result["tx_hash"] == "0xFakeTxHash"
    assert result["status"] == "pending"

def test_lulo_unstake():
    web3 = MagicMock(spec=Web3)
    web3.toWei = Web3.toWei
    web3.eth.contract.return_value.functions.unstake.return_value.build_transaction.return_value = {
        'from': '0xUserAddress',
        'gas': 200000,
        'gasPrice': Web3.toWei('5', 'gwei')
    }
    web3.eth.send_transaction.return_value.hex.return_value = "0xFakeTxHash"
    
    lulo = LuloProtocol(web3)
    result = lulo.unstake(0.1, "0xUserAddress")
    
    assert result["tx_hash"] == "0xFakeTxHash"
    assert result["status"] == "pending"

def test_lulo_invalid_stake():
    web3 = MagicMock(spec=Web3)
    lulo = LuloProtocol(web3)
    
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        lulo.stake(0, "0xUserAddress")

def test_lulo_invalid_unstake():
    web3 = MagicMock(spec=Web3)
    lulo = LuloProtocol(web3)
    
    with pytest.raises(ValueError, match="Token amount must be greater than zero"):
        lulo.unstake(0, "0xUserAddress")
