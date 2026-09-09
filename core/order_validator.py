from core.orders import OrderRequest


class OrderValidator:

    def validate(self, order: OrderRequest, symbol_info):

        if order.volume < symbol_info.volume_min:
            raise ValueError(
                f"Volume {order.volume} is below minimum "
                f"{symbol_info.volume_min}"
            )

        if order.volume > symbol_info.volume_max:
            raise ValueError(
                f"Volume {order.volume} is above maximum "
                f"{symbol_info.volume_max}"
            )

        step = symbol_info.volume_step

        if round(order.volume / step) * step != order.volume:
            raise ValueError(
                f"Volume {order.volume} does not match "
                f"volume step {step}"
            )

        return True