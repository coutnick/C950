class Truck():
    def __init__(self, truck_id, loaded_packages, distance, max_capacity, capacity): #implement time here or globally
        self.truck_id = truck_id
        self.loaded_packages = loaded_packages
        self.distance = distance
        self.max_capacity = max_capacity
        self.capacity = capacity

    def __str__(self):
        return f"Truck ID: {self.truck_id} Packages: {self.loaded_packages} Distance: {self.distance}  Max Capacity: {self.max_capacity} Capacity: {self.capacity}"
    
    def packages_on_truck(truck):
        for package in truck.loaded_packages:
            print(package)