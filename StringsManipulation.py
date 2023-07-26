# LESSON PLAN - PYTHON LEVEL 1
# SESSION 4 - STRINGS: MANIPULATING & FORMATTING
# ● String literals: A string is a sequence of characters and they are
# immutable.
# Example: strings = "This is Python"
# print (strings)
# Output: This is Python
# ● Slicing Strings: Slicing refers to obtaining a sub-string from the given
# string.
# ○ slice( ) method and array slice [:] are commonly used.
# ● Slice( ) Method:
# Syntax: slice(stop)
# slice(start, stop, step)
# ● Parameters:
# ○ start: Starting index where the slicing of object starts.
# ○ stop: Ending index where the slicing of object stops.
# ○ step: It is an optional argument that determines the increment
# between each index for slicing.
# ○ Return Type: Returns a sliced object containing elements in the
# given range only.
# Example: String = 'ASTRING’
# s2 = slice(1, 5, 2)
# print(String[s2])
# Output: SR
# ● Array slice[:] method: Indexing syntax can be used as a substitute for
# the slice object.
# Syntax: arr[start:stop]
# Example:
# string1 = "Python Programming"
# print(string1[0:6])
# print(string1[7:])
# print(string1[:6])
# print(string1[:])
# print(string1[::-1])
# Output: Python
# Programming
# Python
# Python Programming
# gnimmargorP nohtyP
# ● String Concatenation: Concatenation (+ Operator) refers to the
# joining or merging of two or more strings.
# Example: "welcome" + "Python"
# Output: 'welcomePython'
# ○ The join() is a string method that is used to join a sequence of
# elements.
# Example: s1 , s2 = "Python" , “Program”
# s3="".join([s1,s2])
# Output: PythonProgram
# ● String formatting using format(): The format() method formats the
# specified value(s) and insert them inside the string's placeholder.
# Example:
# num1=int (input("Number 1: "))
# num2=int (input("Number 2: "))
# print ("The sum of { } and { } is { }".format(num1, num2,(num1+num2)))
# Output: Number 1: 34
# Number 2: 54
# The sum of 34 and 54 is 88
# ● Build- in string functions:
# ● Escape sequence : Escape sequences are formed using two things: the
# first is a backslash (\), and the second is the set of one or more characters
# following that backslash (\t).
# Example: To print the message "It's raining", the Python command is
# >>> print ("It\'s raining")
# Output: It's raining
# ● fstring : f-strings provide a faster, more readable, more concise, and less
# error prone way of formatting strings in Python.
# Example: bags = 3
# apples_in_bag = 12
# print(f ' There are total of {bags * apples_in_bag} apples')
# Output: There are total of 36 apples
# A. Class Assignment: Check string is Palindrome or not
# str=input("Enter the string : ") #Enter input as string
# strrev=str[::-1] #Array slice[:] method for reverse string
# print("The reversed string is ",strrev) #Print reverse string
# if(str==strrev): #if input string is equal to reverse string
# print(str,"is a palindrome") #Print that string is a palindrome
# else: #otherwise
# print(str,"is not a palindrome") #Print that string is not a palindrome
# Output:


# signal = BTO 1 ESM3 @ 4285.5

# signal = input("Enter the string : ")
# print("Action is ", signal[0:3])
# print("Quantity is ", signal[4:5])
# print("Symbol is ", signal[6:9])
# print("Price is ", signal[12:17])
# print("Date is ", signal[18:28])
# print("Time is ", signal[29:34])
# print("User is ", signal[35:])

# string1 = "Python Programming"
# print(string1[0:6])
# print(string1[7:])
# print(string1[:6])
# print(string1[:])
# print(string1[::-1])

s1 , s2 = "Python" , "Program"
s3="".join([s1,s2])
print(s3)

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))



    #    pattern = f"({p})"+"\s?(\d+)?\s?(\w+)\s+(?:(\d+(?:\.\d+)?)(\w))?\s?(\d{1,2}/\d{1,2}(?:/\d{4})?)(?:/\d+)?\s?(?:@\s?(?:((?:\d+)?(?:\.\d+)?)))?"
    #     content = message.content
    #     data = re.findall(pattern, content, re.M)
    #     for i in data:
    #         print(i)
    #         row = [str(message.channel.id), str(message.author.id),
    #                 datetime.now().strftime('%m/%d/%Y %H:%M:%S')]
    #         if i[0] in ["BTO", "STO"]:      
    #             row.append("1")
    #         elif i[0] in ["STC","BTC"]: 
    #             row.append("-1")
    #         else:
    #             row.append("Null")
    #         row.append(i[1]) if i[1] else row.append("Null")
    #         d = i[5].split("/")
    #         d1 = d[0].zfill(2)
    #         d2 = d[1].zfill(2)
    #         row.append(
    #             f"{i[2]}_{i[2]}S 23{d1}{d2} {i[4]} {i[3]}".upper())
    #         row.append(i[6]) if i[6] else row.append("Null")
    #         row.extend(["", "pending", message.author.name, message.channel.name])
    #         dataframes.append(row)