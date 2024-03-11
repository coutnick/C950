import csv
from datetime import timedelta
from package import Package
from truck import Truck
from chaining_hash import ChainingHashTable

# Read package data from csv file
with open("Data/package_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    package_data = []
    for row in csv_reader:
        package_data.append(row)
         
# read distance data from csv file        
with open("Data/distance_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    distance_data = []
    for row in csv_reader: 
        dist_list = [float(x) for x in row [0: :] if x != ""]
        distance_data.append(dist_list)

# read distance data from csv file
with open("Data/address_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    address_data = []
    for row in csv_reader: 
        address_data.append(row[2])

# print(package_data)

# Create list of packages
packages = Package.load_package(package_data)

      
# Creates a hash table to store all of the packages
package_hash = ChainingHashTable()

for package in packages:
     package_hash.insert(package.package_id, package)


for i in range(1, len(package_hash.table) + 1):
     print(package_hash.search(str(i)))



truck_one_packages = [1, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]

truck_one = Truck(1, truck_one_packages, 0, 16, len(truck_one_packages))

print(truck_one)

#come up with distance formulas

