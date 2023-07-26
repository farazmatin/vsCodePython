# June 13, 2023
# Write a program to print the cube of all the numbers from 1 to the given number.
# Write a program to print the square -of all the numbers from 1 to the given number.
# Write a program to print the square root of all the numbers from 1 to the given number.
# Write a program in which you have to use two counters. Counter 1 should be incremented by 1 if any even number is encountered. Counter 2 should be incremented by 3 if any odd value is encountered. Do it for all the natural numbers till 100.
# Write a program for Fibonacci Sequence.
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.


num = int(input("Please enter a number: "))
for i in range(1,num+1):
    print(i**3)
