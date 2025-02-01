from typing import Type, Dict
from .aave import AaveProtocol
from .lido import LidoProtocol
from .lulo import LuloProtocol
from .uniswap import UniswapProtocol

class UnsupportedProtocolError(Exception):
    pass

LENDING_PROTOCOLS: Dict[str, Type] = {
    "aave": AaveProtocol,
    "lulo": LuloProtocol,
}

STAKING_PROTOCOLS: Dict[str, Type] = {
    "lido": LidoProtocol,
}

DEX_PROTOCOLS: Dict[str, Type] = {
     "uniswap": UniswapProtocol, 
}

def get_lending_protocol(name: str):
    name = name.lower()
    if name not in LENDING_PROTOCOLS:
        raise UnsupportedProtocolError(f"Unsupported lending protocol: {name}")
    return LENDING_PROTOCOLS[name]()

def get_staking_protocol(name: str):
    name = name.lower()
    if name not in STAKING_PROTOCOLS:
        raise UnsupportedProtocolError(f"Unsupported staking protocol: {name}")
    return STAKING_PROTOCOLS[name]()

def get_dex_protocol(name: str):
    name = name.lower()
    if name not in DEX_PROTOCOLS:
        raise UnsupportedProtocolError(f"Unsupported DEX protocol: {name}")
    return DEX_PROTOCOLS[name]()
