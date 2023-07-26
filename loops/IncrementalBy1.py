# Write a program in which you have to use two counters. 
# Counter 1 should be incremented by 1 if any even number is encountered. 
# Counter 2 should be incremented by 3 if any odd value is encountered. 
# Do it for all the natural numbers till 100.

counter1 = 0
counter2 = 0
num = int(input("Please enter a number: "))


for i in range(1,num+1):
    if i%2 == 0:
       counter1 +=1
    else:
       counter2 +=3
print(counter1)
print(counter2)    