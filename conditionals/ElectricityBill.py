# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              $ 5 per unit
# After 200 units                                             $ 10 per unit
# (For example if input unit is 350 than total bill amount is $ 2000)

units = float(input("Enter number of units: "))
if units <= 100:
    print("No charge")
elif units >= 100 and units <= 200:
    bill = (units-100)*5
    print(bill)
elif units > 200:
    bill = 500 + (units-200)*10
    print(bill)
else:
    print("")



# 100 - $0
# 100 - 5 x 100 = 500
# 150 = 10 x 150 = 1500