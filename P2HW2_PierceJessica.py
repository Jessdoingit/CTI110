# Jessica Pierce
# 06/28/2026
# P2HW2
# Understanding lists.

# Pseudocode
# 1. Ask user to enter six module grades.
# 2. Create a list.
# 3. Display the lowest grade.
# 4. Display the highest grade.
# 5. Display the sum of all grades.
# 6. Display the average grade.
# 7. Display the results.

#Ask user to enter six module grades.
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#Create a list.
grades = [module1, module2, module3, module4, module5, module6]

#Display the lowest grade in the list.
lowest = min(grades)

#Display the hightest grade in the list.
highest = max(grades)

#Display the sum of all grades.
total = sum(grades)

#Display the grades average.
average = total / len(grades)

#Display the results.
print("\n------------Results------------")
print(f"{'Lowest Grade:':20}{lowest}")
print(f"{'Highest Grade:':20}{highest}")
print(f"{'Sum of Grades:':20}{total}")
print(f"{'Average:':20}{average:.2f}")

print()


