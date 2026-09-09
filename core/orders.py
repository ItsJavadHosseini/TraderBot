from dataclasses import dataclass
from enum import Enum


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"


@dataclass
class OrderRequest:
    symbol: str
    side: OrderSide
    volume: float
    order_type: OrderType = OrderType.MARKET
    stop_loss: float | None = None
    take_profit: float | None = None