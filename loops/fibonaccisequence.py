# Write a program for Fibonacci Sequence.
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

# First term: 0
# Second term: 1
# Third term: (0+1)= 0
# Fourth term: (1+1)=2
# Fifth term: (2+1)=3



fibonacci1 =   0
fibonacci2 =   1

for i in range (1,9):
    fibonacci3 = fibonacci1 + fibonacci2 
    print (fibonacci3)
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3
    
    
    
