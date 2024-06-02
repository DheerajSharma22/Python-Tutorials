# Input function is used to take input in python and also you can provide a string in it to prompt the input message to user.

num = input("Enter first num :- ")
print(num)
print(type(num)) # Input function always takes input as an string

# We have to expilcitly convert it into int to make it integer
num = int(num)
print(type(num))