import csv
from package import Package
from chaining_hash import ChainingHashTable

# Read package data from csv file
package_data = Package.read_package_data("package_data.csv")



loaded_packages = Package.load_package(package_data)

# Initialize and load a hash table with package
myHash = ChainingHashTable()

for package in loaded_packages:
    myHash.insert(package.package_id, package)


for i in range(len(myHash.table) + 1):
    print(myHash.search(str(i)))

with open("distance_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    distance_data = []
    for row in csv_reader: 
        distance_data.append(row)

with open("address_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    address_data = []
    for row in csv_reader: 
        address_data.append(row)


print(len(address_data))
print(len(distance_data))


    