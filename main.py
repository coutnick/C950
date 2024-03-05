from package import Package
from chaining_hash import ChainingHashTable

package_data = Package.read_package_data("package_data.csv")

loaded_packages = Package.load_package(package_data)

myHash = ChainingHashTable()

for package in loaded_packages:
    myHash.insert(package.package_id, package)

for i in range(1, 41):
    print(myHash.search(str(i)))


    