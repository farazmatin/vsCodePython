# Write a Python program to print the number of days for every month name you take as an input from the user.


month = input("Enter month name: ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 days")
elif month == "February":
    print("28 days")
else:
    print("Please enter correct month name")