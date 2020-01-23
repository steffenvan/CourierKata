class ShippingPriceInfo:
    def __init__(self, price: float, weight_limit: float, overweight_price: float):
        self.price = price
        self.weight_limit = weight_limit
        self.overweight_price = overweight_price