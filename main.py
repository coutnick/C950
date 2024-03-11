import csv
from datetime import timedelta
from package import Package
from truck import Truck
from chaining_hash import ChainingHashTable

def get_distance(index_1, index_2):
    try:
        return distance_data[index_1][index_2]
    except:
        return distance_data[index_2][index_1]
    
def get_address_index(address):
    return address_data.index(address)

def get_shortest_distance(starting_address, package_id_list, package_hash):
    closest_distance = 100
    closest_destination = ""
    package_to_remove = 0
    package_list = package_id_list
    starting_index = get_address_index(starting_address)

    for package_id in package_list:
        package = package_hash.search(str(package_id))
        destination_index = get_address_index(package.address)
        distance = get_distance(starting_index, destination_index)
        
        if distance < closest_distance:
            closest_distance = distance
            closest_destination = package.address
            package_to_remove = package_id

    return closest_distance, closest_destination, package_to_remove

def deliver_packages(truck, package_hash):
    truck_packages = truck.loaded_packages

    while len(truck_packages) != 0: 
        delivery = get_shortest_distance(truck.address, truck_packages, package_hash)
        miles = delivery[0]
        address = delivery[1]
        id = delivery[2]
        truck_packages.remove(id)
        time_to_deliver = miles / 18
        truck.start_time += timedelta(hours=time_to_deliver)
        truck.mileage += miles
        truck.address = address
        delivered_package = package_hash.search(str(id))
        delivered_package.status = "Delivered"
        delivered_package.delivery_time = truck.start_time
        package_hash.insert(id, delivered_package)
    
    return truck.start_time
    
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


# Set the start time
start_time = timedelta(hours=8, minutes=0, seconds=0)



# Create list of packages
packages = Package.load_package(package_data)

      
# Creates a hash table to store all of the packages
package_hash = ChainingHashTable()

for package in packages:
     package_hash.insert(package.package_id, package)

truck_one_packages = [1, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]

truck_two_packages = [3, 18, 36, 38, 15, 19, 13, 14, 16, 20, 29, 30, 31, 33, 34, 35]

truck_three_packages = [6, 9, 25, 28, 32, 37, 39, 40]

truck_one = Truck(1, truck_one_packages, "4001 South 700 East", 0, start_time)
truck_two = Truck(2, truck_two_packages, "4001 South 700 East", 0, timedelta(hours=9, minutes=5))




