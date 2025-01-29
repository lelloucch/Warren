from .stake import stake_template
from .lending import supply_template, withdraw_template
from .dex import add_liquidity_template, remove_liquidity_template

__all__ = [
    "stake_template",
    "supply_template", "withdraw_template",
    "add_liquidity_template", "remove_liquidity_template"
]
