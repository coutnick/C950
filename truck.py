
class Truck():
    def __init__(self, truck_id, loaded_packages, address, mileage, start_time, current_time): 
        self.truck_id = truck_id
        self.loaded_packages = loaded_packages
        self.address = address
        self.mileage = mileage
        self.start_time = start_time
        self.current_time = start_time

    def __str__(self):
        return f"{self.loaded_packages}, {self.address}, {self.mileage}, {self.start_time}, {self.current_time}"
       
    
    