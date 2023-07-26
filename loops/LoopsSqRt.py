# Write a program to print the square root of all the numbers from 1 to the given number.
#math.sqrt

import math
num = int(input("Please enter a number: "))
for i in range(1,num+1):
    print(math.sqrt(i))
    