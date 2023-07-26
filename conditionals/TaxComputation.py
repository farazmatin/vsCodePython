# Write a program to implement a choice-based program to compute the tax to be paid on a given salary per annum.
# Tax Slabs - No tax below an income of $50000
# 20% tax for income in the range of $50000 - $100000
# 35% tax for all the incomes above $100000


salary = int(input("Please enter salary: "))
if salary < 50000:
    print("No tax applicable")
elif salary >= 50000 and salary <= 100000:
    print("Tax percent is 20% ", "Tax payable is $", salary * .2)
elif salary > 100000:  
    print("Tax percent is 35%", "$", salary * .35)
else:
    print("Please input correct salary")
    