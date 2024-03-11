import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, delivery_time=None, loaded_time=None, status="At the Hub", on_truck=None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.on_truck = on_truck
        self.delivery_time = delivery_time
        self.loaded_time = loaded_time

    def __str__(self):
        return f"""Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code},
             Deadline: {self.deadline}, Weight: {self.weight}, Notes: {self.notes}, Status: {self.status}, On Truck: {self.on_truck}, delivery time: {self.delivery_time}, loaded time: {self.loaded_time}"""
    
    def load_package(package_data):
        packages = []
        for row in package_data:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.append(package)
        return packages
    
