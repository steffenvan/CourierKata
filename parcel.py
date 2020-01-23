class Parcel:
    def __init__(self, height, width):
        self.height = height
        self.width = width 
        self.parcel_type = "None"
    
    def get_max_dim(self):
        return max(self.height, self.width)

    def get_parcel_type(self):
        max_dim = self.get_max_dim()
        if max_dim < 10:
            self.parcel_type = "Small"
        elif max_dim < 50:
            self.parcel_type = "Medium"
        elif max_dim < 100:
            self.parcel_type = "Large"
        else:
            self.parcel_type = "XLarge"