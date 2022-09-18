# Hash enables to write single line comments
# Take input from console
# Pthon is dynamic typed lanuage. User doesn't need to define data type of the variable. Interpreter automatically assigns variable data type, this however makes interpreter slow.
"""
Multiline Doc string
Description: This code describes to take input from user. And check data type
"""
# \n ---> newline  ---> It causes a line break
var = input("Enter your Input\n")
print(f"Data type of your input is: {var}", f"The input is: {var}", sep=",\n")

name = input("Enter your name\n")
print(f"Data type of input is: {type(name)}")
print(f"Your name is: {name}", sep="")

# Accept only int data type
# cast input function with the data type you need. This will raise exception if you provide string
number = int(input("Enter number"))
print(f"Number is: {number}")