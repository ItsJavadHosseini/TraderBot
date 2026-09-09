from core.order_validator import OrderValidator


class TradingEngine:

    def __init__(self, broker):
        self.broker = broker
        self.validator = OrderValidator()

    def execute(self, order):

        symbol_info = self.broker.get_symbol_info(
            order.symbol
        )

        self.validator.validate(
            order,
            symbol_info
        )

        return self.broker.place_order(order)