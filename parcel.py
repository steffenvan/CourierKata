from shipping_price_info import ShippingPriceInfo

class Parcel:
    def __init__(self, height, width, weight = 0):
        self.height = height
        self.width = width 
        self.parcel_type = "None"
        self.price = 0
        self.weight = weight
        self.set_parcel_type()
    
    def get_max_dim(self):        
        return max(self.height, self.width)

    def set_parcel_type(self):
        """Sets the type for a parcel with the initialised dimensions 
        >>> p = Parcel(10, 10)
        >>> print(p.get_parcel_type())
        Medium
        """
        max_dim = self.get_max_dim()
        if max_dim < 10:
            self.parcel_type = "Small"
        elif max_dim < 50:
            self.parcel_type = "Medium"
        elif max_dim < 100:
            self.parcel_type = "Large"
        else:
            self.parcel_type = "XLarge"

        if self.weight >= 50:
            self.parcel_type = "Heavy"

    def get_parcel_type(self):
        return self.parcel_type

    # Shipping info: Dict[str, ShippingPriceInfo]
    def set_price(self, shipping_infos):
        if self.parcel_type not in shipping_infos:
            raise Exception("This parcel type does not have a shipment rate yet!")
        
        shipping_info = shipping_infos[self.parcel_type]
        self.price = shipping_info.price
        self.price += self.get_overweight_price(shipping_info)

    def get_price(self):
        return self.price

    def get_overweight_price(self, shipping_info):
        """Returns a new price if the parcel's weight exceeds its type's weight limit. 
        >>> p = Parcel(60, 50, 8)
        >>> print(p.get_overweight_price())
        4
        """
        weight_limit = shipping_info.weight_limit
        extra_price = 0
        if self.weight > weight_limit:
            excessive_weight = self.weight - weight_limit
            overweight_rate = shipping_info.overweight_price
            extra_price = excessive_weight * overweight_rate

        return extra_price