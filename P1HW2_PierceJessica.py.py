# Jessica Pierce
# 06/28/2026
# P1HW2
# Travel budget after expenses.

# Questions

# Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results


# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses
expenses = gas + hotel + food
remaining = budget - expenses

# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)

print("\nFuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)

print("---------------------------------------")
print("Remaining Balance:", remaining)