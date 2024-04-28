import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, delivery_time=None, status="At the Hub", on_truck="N/A"):
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
        address = (self.address[:30] + '...') if len(self.address) > 33 else self.address
        notes = (self.notes[:15] + '...') if self.notes and len(self.notes) > 18 else self.notes
        delivery_time = self.delivery_time if self.delivery_time else "N/A"
        return f"{self.package_id:<3}  {address:<35} {self.city:<20} {self.state:<5} {self.zip_code:<10} {self.deadline:<10} {self.weight:<6} {notes:<20} {self.status:<10} {self.on_truck:<5} {delivery_time}"
    
    def load_package(package_data):
        packages = []
        for row in package_data:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.append(package)
        return packages
    
    def package_header(self):
        header = f"{'ID':<3}  {'Address':<35} {'City':<20} {'State':<5} {'Zip':<10} {'Deadline':<10} {'Weight':<6} {'Notes':<20} {'Status':<10} {'Truck':<5} {'Delivery Time'}"
        return header
    
