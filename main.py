'''WGUPS delivery system
    Author: Nicholas Rains
    Date: 4/8/2024
    Student ID: 010471828'''
import csv
from datetime import timedelta
from package import Package
from truck import Truck
from chaining_hash import ChainingHashTable

HUB_ADDRESS = "4001 South 700 East"
TRUCK_ONE_START = timedelta(hours=8, minutes=0)
TRUCK_TWO_START = timedelta(hours=9, minutes=5)

    # Read package data from csv file
with open("package_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    package_data = []
    for row in csv_reader:
        package_data.append(row)
        
# read distance data from csv file        
with open("distance_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    distance_data = []
    for row in csv_reader: 
        dist_list = [float(x) for x in row [0: :] if x != ""]
        distance_data.append(dist_list)

# read distance data from csv file
with open("address_data.csv", "r", encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    address_data = []
    for row in csv_reader: 
        address_data.append(row[2])

# Get the distance from the 2-d matrix of distances
def get_distance(index_1, index_2):
    try:
        return distance_data[index_1][index_2]
    except:
        return distance_data[index_2][index_1]

# Get the address index
def get_address_index(address):
    return address_data.index(address)

# Find the shortest distance. This algorithm finds the shortest distance from the current destination. 
    #Parameters: Starting address-starting address location, Package_id_list-To find package address, package-hash-the package hash table
    #Returns: Closest distance, closest_destination, package_to_remove
def get_shortest_distance(starting_address, package_id_list, package_hash):
    closest_distance = 100
    closest_destination = ""
    package_to_remove = 0
    package_list = package_id_list
    starting_index = get_address_index(starting_address)

    # Iterate through the package list and find the closest destination
    for package_id in package_list:
        package = package_hash.search(str(package_id))
        destination_index = get_address_index(package.address)
        distance = get_distance(starting_index, destination_index)
        # If the distance is less than the closest distance then update the closest distance and destination
        if distance < closest_distance:
            closest_distance = distance
            closest_destination = package.address
            package_to_remove = package_id

    return closest_distance, closest_destination, package_to_remove

#Algorithm to deliver the packages. Delivers packages on the truck and returns the miles and current time. Will iterate until a seach time is reached or the packages on the truck are empty
#Params: truck-the truck that is delivering pacakges, pacakge_hash-the hashtable with packages, seach-time(optional)-used to stop the delivery and/or update status and address of pacakge 9
#Returns: Trucks current time and trucks current mileage
def deliver_packages(truck, package_hash, search_time=None):
    truck_packages = truck.loaded_packages
    
    # Set the packages on the truck to en route
    for package in truck_packages:
        package_on_truck = package_hash.search(str(package))
        package_on_truck.on_truck = truck.truck_id
        package_on_truck.status = "En Route"
        package_hash.insert(package_on_truck.package_id, package_on_truck)

    # Iterate through the packages on the truck
    while len(truck_packages) != 0:
        
        # Update package 9 address at 10:20 am
        if truck.truck_id == 3 and truck.current_time >= timedelta(hours=10, minutes=20):
            new_address = "410 S State St"  #update this packages address at 10:20 am
            package_to_update = package_hash.search(str(9))
            package_to_update.address = new_address
            package_hash.insert(6, package_to_update)
        
        # If the search time is reached then break the loop
        if search_time and (truck.current_time >= search_time): 
                break
        
        delivery = get_shortest_distance(truck.address, truck_packages, package_hash)
        miles = delivery[0]
        address = delivery[1]
        id = delivery[2]
        truck_packages.remove(id)
        
        truck.current_time += timedelta(hours=miles / 18)
        truck.mileage += miles
        truck.address = address
        delivered_package = package_hash.search(str(id))
        delivered_package.status = "Delivered"
        delivered_package.delivery_time = truck.current_time
        package_hash.insert(id, delivered_package)
        
    return truck.current_time, truck.mileage


class Main():
    while True:
        # Set the start time
        start_time = timedelta(hours=8, minutes=0, seconds=0)

        # Create list of packages
        packages = Package.load_package(package_data)
            
        # Creates a hash table to store all of the packages
        package_hash = ChainingHashTable()

        for package in packages:
            package_hash.insert(package.package_id, package)

        # Manually load the trucks
        truck_one_packages = [1, 13, 14, 15, 19, 16, 2, 4, 5, 7, 8, 30, 37]
        truck_two_packages = [18, 3, 36, 38, 10, 12, 11, 17, 20, 21, 22, 23, 24, 26,27]
        truck_three_packages = [6, 9, 25, 28, 32, 29, 31, 33, 34, 35,  39, 40]

        # Create the trucks
        truck_one = Truck(1, truck_one_packages, HUB_ADDRESS, 0, TRUCK_ONE_START, TRUCK_ONE_START)
        truck_two = Truck(2, truck_two_packages, HUB_ADDRESS, 0, TRUCK_TWO_START, TRUCK_TWO_START)
        truck_three = Truck(3, truck_three_packages, HUB_ADDRESS, 0, TRUCK_ONE_START, TRUCK_ONE_START)
        

        trucks = [truck_one, truck_two, truck_three]

        
        print("""                   Welcome to WGUPS Delivery System
            -----------------------------------------         
        1. Print All Package Status and Total Miles
        2. Get a Single Package Status with a time
        3. Get All Package Status with a Time
        4. Exit
            -----------------------------------------
        """)
        user_selection = int(input("What would you like to do? "))

    

        if user_selection == 4: #Exit the program
            print('Thanks for using WGUPS delivery management system. Goodbye!')
            break

        if user_selection == 1:
            truck_one_result = deliver_packages(truck_one, package_hash)
            truck_two_result = deliver_packages(truck_two, package_hash)
            first_to_finish = min(truck_one_result[0], truck_two_result[0])  # find the first trucks time to finish
            truck_three = Truck(3, truck_three_packages, HUB_ADDRESS, 0, first_to_finish, first_to_finish) # Set this trucks time and start time to the first trucks finishing time
            truck_three_result = deliver_packages(truck_three, package_hash)
            
            print(package.package_header())
            for i in range(1, 41):
                print(package_hash.search(str(i)))

            print("Total Mileage: " + str(truck_one_result[1] + truck_two_result[1] + truck_three_result[1]))
        
        elif user_selection == 2:
            
            package_query = int(input("Please Enter a package ID "))
            search_time_list = input("Please enter a time in the format HH:MM:SS ").split(":")
            search_time = timedelta(hours=int(search_time_list[0]), minutes=int(search_time_list[1]), seconds=int(search_time_list[2]))
            print(package.package_header())

            # Iterate through the trucks and deliver the packages
            for truck in trucks:
                if package_query in truck.loaded_packages:
                    if truck.truck_id == 1 or truck.truck_id == 2:
                        if search_time < TRUCK_TWO_START:  # If the seach time is before truck twos start time then only deliver trucks on truck 1
                            deliver_packages(truck_one, package_hash, search_time) 
                            print(package_hash.search(str(package_query)))
                            break
                        deliver_packages(truck_one, package_hash, search_time)
                        deliver_packages(truck_two, package_hash, search_time)
                        print(package_hash.search(str(package_query)))

                    #If the search time is after 9:20 am then deliver packages on truck one, truck two, and truck three
                    elif truck.truck_id == 3:
                        truck_one_result = deliver_packages(truck_one, package_hash)
                        truck_two_result = deliver_packages(truck_two, package_hash)
                        first_to_finish = min(truck_one_result[0], truck_two_result[0])
                        print(first_to_finish)

                        truck_three.current_time = first_to_finish
                        truck_three.start_time = first_to_finish

                        deliver_packages(truck_three, package_hash, search_time)

                        print(package_hash.search(str(package_query)))
        
        elif user_selection == 3:
            search_time_list = input("Please enter a time in the format HH:MM:SS ").split(":")
            search_time = timedelta(hours=int(search_time_list[0]), minutes=int(search_time_list[1]), seconds=int(search_time_list[2]))

            #If the search time is before 9:05 am then deliver packages on truck one
            if search_time < TRUCK_TWO_START:   
                truck_one_result = deliver_packages(truck_one, package_hash, search_time) 
                print(package.package_header())
                for i in range(1, 41):
                    print(package_hash.search(str(i)))

                print("Total Mileage: " + str(truck_one_result[1]))

            #If the search time is before 9:20 am then deliver packages on truck one and truck two
            elif search_time < timedelta(hours=9, minutes=20, seconds=20): #
                truck_one_result = deliver_packages(truck_one, package_hash, search_time)
                truck_two_result = deliver_packages(truck_two, package_hash, search_time)
                print(package.package_header())
                for i in range(1, 41):
                    print(package_hash.search(str(i)))
                print("Total Mileage: " + str(truck_one_result[1] + truck_two_result[1]))

            #If the search time is after 9:20 am then deliver packages on truck one, truck two, and truck three
            else:
                truck_one_result = deliver_packages(truck_one, package_hash, search_time)
                truck_two_result = deliver_packages(truck_two, package_hash, search_time)
            
                first_to_finish = min(truck_one_result[0], truck_two_result[0])

                truck_three = Truck(3, truck_three_packages, HUB_ADDRESS, 0, first_to_finish, first_to_finish)
                truck_three_result = deliver_packages(truck_three, package_hash, search_time)
                
                print(package.package_header())
                for i in range(1, 41):
                    print(package_hash.search(str(i)))

                print("Total Mileage: " + str(truck_one_result[1] + truck_two_result[1] + truck_three_result[1]))
        else:
            print("Invalid. Please Try again")

                



        
            
            
            

        

