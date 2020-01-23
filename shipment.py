from parcel import Parcel

class Shipment: 
    def __init__(self):
        self.normal_orders = []
        self.fast_orders = []
        self.total_shipment_price = 0
    
        
    def set_shipment_rate(self, parcels: List[Parcel], parcel_rates: Dict[ParcelType, rate], fast_delivery = False): 
        for parcel in parcels:
            parcel.set_price()
            self.total_shipment_price += parcel.price

        if fast_delivery:
            self.total_shipment_price *= 2 