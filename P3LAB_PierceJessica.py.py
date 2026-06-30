# Jessica Pierce
# 06/29/2026
# P3LAB
# Enter a money (float) value with two places after the decimal.

#Input from user
amount = float(input("Enter a dollar amount (ex: 12.34): "))

#Convert to cents
total_cents = int(round(amount * 100))

#Calculate coins
dollars = total_cents // 100
remainder = total_cents % 100

quarters = remainder // 25
remainder = remainder % 25

dimes = remainder // 10
remainder = remainder % 10

nickels = remainder // 5
pennies = remainder % 5

#Output results
if dollars > 0:
    print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")

if quarters > 0:
    print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")

if dimes > 0:
    print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")

if nickels > 0:
    print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")

if pennies > 0:
    print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")

    