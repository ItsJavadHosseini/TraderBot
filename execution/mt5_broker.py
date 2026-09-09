import MetaTrader5 as mt5
from datetime import datetime

from core.market_data import MarketData
from .broker import Broker


class MT5Broker(Broker):

    def get_price(self, symbol):

        tick = mt5.symbol_info_tick(symbol)

        if tick is None:
            raise RuntimeError(
                f"Could not get price for {symbol}"
            )

        return MarketData(
            symbol=symbol,
            bid=tick.bid,
            ask=tick.ask,
            timestamp=datetime.fromtimestamp(tick.time)
        )

    def place_order(self, symbol):
        pass

    def get_symbol_info(self, symbol):
        info = mt5.symbol_info(symbol)

        if info is None:
            raise RuntimeError(
                f"Could not get symbol info for {symbol}"
            )

        return info