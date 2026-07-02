# Jessica Pierce
# 07/01/2026
# P3HW1
# Debugging assignment


#Enter grades for six modules
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))


#Create list to add grades
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


#Caluclate the grades
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)


#Determine letter grades
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"


#Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")
print("--------------------------------")
print(f"Your grade is: {letter_grade}")




