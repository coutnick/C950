import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, delivery_time=None, status="At the Hub", on_truck=None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = delivery_time
        self.on_truck = on_truck
        

    def __str__(self):
        return f"{self.package_id},  {self.address},  {self.city},  {self.state},  {self.zip_code},  {self.deadline},  {self.weight}, {self.notes},  {self.status},  {self.on_truck},  {self.delivery_time}"
    
    def load_package(package_data):
        packages = []
        for row in package_data:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.append(package)
        return packages
    
