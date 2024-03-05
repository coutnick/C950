from package import Package

package_data = Package.read_package_data("package_data.csv")

loaded_packages = Package.load_package(package_data)

for package in loaded_packages:
    print(package)




    