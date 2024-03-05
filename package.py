import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, delivered=False):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.deliverd = delivered

    def __str__(self):
        return f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight}, Notes: {self.notes}, Delivered: {self.deliverd}"
    

    def read_package_data(csv_file):
        with open(csv_file, "r", encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)
            package_data = []
            for row in csv_reader:
                package_data.append(row)
            return package_data
        
    def load_package(package_data):
        packages = []
        for row in package_data:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.append(package)
        return packages
    
