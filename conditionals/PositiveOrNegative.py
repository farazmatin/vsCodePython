# Write a program to check whether a number is positive, negative or zero.

number = int(input("Enter a number: "))

# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")
# else:
#     print("Number is zero")

if number >= 0:
    print("Number is either a zero or a positive")
else:
    print("Number is a negative")