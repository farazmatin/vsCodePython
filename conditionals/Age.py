# Take input of the age of 3 people by user and determine oldest among them.

age1 = int(input("Please input age: "))
age2 = int(input("Please input age: "))
age3 = int(input("Please input age: "))

if age1 >  age2 and age1 > age3:
    print("User 1 is oldest")
elif age2 >  age1 and age2 > age3:
    print("User 2 is oldest")
elif age3 >  age1 and age3 > age2:
    print("User 3 is oldest")
else:
    print("Cant decide")