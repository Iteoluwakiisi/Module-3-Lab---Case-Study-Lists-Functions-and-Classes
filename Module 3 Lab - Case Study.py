"""
Name: Iteoluwakiisi George Olaniyan
File Name: Module 3 Lab - Case Study
Description: This Python program allows users to input details for different types of vehicles. 
The program collects user input for the vehicle type, year, make, model, number of doors, and roof type, 
stores this information in an object, then it outputs the details in a clear and easy-to-read format.

""" 

class Vehicle:      # Define the Vehicle superclass
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):   # Define the Automobile class
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def create_automobile():        # Function to collect user input and create an Automobile object
    vehicle_type = input("Enter the type of vehicle(car, truck, plane, boat, or broomstick): ")
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile()      # Create an empty Automobile object

    # Set the vehicle type and other attributes
    car.set_vehicle_type(vehicle_type)
    car.set_attributes(year, make, model, doors, roof)
    
    # Display the vehicle information
    print("\nVehicle details:")
    car.display_info()

create_automobile()     # Call the function to create and display the vehicle
