# Write a program to print the sum of all the odd numbers from 1 to 50.

sum = 0
for i in range (1,51):
    if (i % 2) != 0:
        sum += i
print("Sum of even numbers is: ", sum)
