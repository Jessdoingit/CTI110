# Jessica Pierce
# 06/28/2026
# P2HW1
# Change how results are displayed.

#Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses
expenses = gas + hotel + food
remaining = budget - expenses

#Display results
print()
print("------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':20}${remaining:.2f}")


