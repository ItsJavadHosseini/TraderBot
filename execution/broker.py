class Broker:

    def get_price(self, symbol):
        raise NotImplementedError
    def place_order(self, symbol):
        raise NotImplementedError

    
    def close_position(self, symbol):
        raise NotImplementedError