from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketData:
    symbol: str
    bid: float
    ask: float
    timestamp: datetime

    @property
    def spread(self) -> float:
        return self.ask - self.bid