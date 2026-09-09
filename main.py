import MetaTrader5 as mt5

from execution.mt5_broker import MT5Broker
from core.orders import OrderRequest, OrderSide
from core.order_validator import OrderValidator


def main():

    # -------------------------
    # 1. Connect to MT5
    # -------------------------
    if not mt5.initialize():
        print("MT5 initialization failed!")
        print(mt5.last_error())
        return

    print("MT5 connected")

    broker = MT5Broker()

    # -------------------------
    # 2. Get Symbol Information
    # -------------------------
    symbol_info = broker.get_symbol_info("EURUSD")

    print("Volume min:", symbol_info.volume_min)
    print("Volume max:", symbol_info.volume_max)
    print("Volume step:", symbol_info.volume_step)
    print("Digits:", symbol_info.digits)
    print("Point:", symbol_info.point)

    # -------------------------
    # 3. Get Market Data
    # -------------------------
    market = broker.get_price("EURUSD")

    print("Symbol:", market.symbol)
    print("Bid:", market.bid)
    print("Ask:", market.ask)
    print("Spread:", market.spread)
    print("Time:", market.timestamp)

    # -------------------------
    # 4. Create Order
    # -------------------------
    order = OrderRequest(
        symbol="EURUSD",
        side=OrderSide.BUY,
        volume=0.1
    )

    print("Order:", order)

    # -------------------------
    # 5. Validate Order
    # -------------------------
    validator = OrderValidator()

    try:
        validator.validate(
            order,
            symbol_info
        )

        print("Order validation: PASSED")

    except ValueError as error:
        print("Order validation: FAILED")
        print("Reason:", error)

    # -------------------------
    # 6. Shutdown MT5
    # -------------------------
    mt5.shutdown()


if __name__ == "__main__":
    main()