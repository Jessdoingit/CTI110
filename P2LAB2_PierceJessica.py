# Jessica Pierce
# 06/28/2026
# P2LAB2
# Write a program that creates a dictionary where the key and value pairs.

#Dictionary
cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

#Variable that holds all keys
keys = cars.keys()

#Print the key variable
print(keys)

#Enter a vehicle
vehicle = input("Enter a vehicle to see its mpg: ")

#Display the mpg
print("The", vehicle, "gets", cars[vehicle], "mpg.")

#Number of miles
miles = float(input("How many miles will you drive?: "))

#Caluclate gallons of gas
gallons = miles  / cars[vehicle]

#Display gallons of gass needed
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle}.")


