from parcel import Parcel
from shipping_price_info import ShippingPriceInfo

class Shipment: 
    # parcels: List[Parcel], shipment_infos: Dict[str, ShippingPriceInfo]
    def __init__(self, parcels, shipment_infos, is_fast_delivery = False):
        self.parcels = parcels
        self.shipment_price = 0
        self.fast_shipment_price = 0
        self.shipment_infos = shipment_infos
        self.is_fast_delivery = is_fast_delivery
        self.set_shipment_price()

    def set_shipment_price(self): 
        for parcel in self.parcels:
            parcel.set_price(self.shipment_infos)
            self.shipment_price += parcel.get_price()

        if self.is_fast_delivery:
            self.fast_shipment_price = self.shipment_price * 2 

    def get_shipment_price(self):
        return self.shipment_price
    
    def get_fast_shipment_price(self):
        return self.fast_shipment_price