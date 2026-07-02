# Jessica Pierce
# 07/01/2026
# P3HW2 Salary
# Caluclate Pay


#Ask for employee name
employee_name = input("Enter employee's name: ")

#Ask for hours worked
hours_worked = float(input("Enter number of hours worked: "))

#Ask for pay rate
pay_rate = float(input("Enter employee's pay rate: "))

#Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay


#Display results of pay
print("-" * 65)
print(f"Employee name: {employee_name}")
print()

print(f"{'Hours Worked':<15}"
      f"{'Pay Rate':<15}"
      f"{'OverTime':<15}"
      f"{'OverTime Pay':<15}"
      f"{'RegHour Pay':<15}"
      f"{'Gross Pay'}")

print("-" * 90)

print(f"{hours_worked:<15.1f}"
      f"${pay_rate:<14.2f}"
      f"{overtime_hours:<15.1f}"
      f"${overtime_pay:<14.2f}"
      f"${regular_pay:<14.2f}"
      f"${gross_pay:.2f}")


