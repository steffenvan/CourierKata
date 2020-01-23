from shipment import Shipment
from shipping_price_info import ShippingPriceInfo
from parcel import Parcel

def get_parcels():
    small_parcel = Parcel(5, 8) # 3 
    medium_parcel = Parcel(25, 30) # 8 
    large_parcel = Parcel(80, 60) # 15
    xlarge_parcel = Parcel(110, 90) # 25 
    heavy_parcel = Parcel(20, 20, 80) # 50 + 30 
    return [small_parcel, medium_parcel, large_parcel, xlarge_parcel, heavy_parcel]

if __name__ == "__main__":
    shipping_infos = {"Small": ShippingPriceInfo(3, 1, 2),
                      "Medium": ShippingPriceInfo(8, 3, 2),
                      "Large": ShippingPriceInfo(15, 6, 2),
                      "XLarge": ShippingPriceInfo(25, 10, 2),
                      "Heavy": ShippingPriceInfo(50, 50, 1)}

    small_parcel = [Parcel(1, 1)]
    small_order = Shipment(small_parcel, shipping_infos)
    assert small_order.get_shipment_price() == 3

    many_parcels = get_parcels()
    shipments = Shipment(many_parcels, shipping_infos)
    assert shipments.get_shipment_price() == 131