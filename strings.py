# In pyton, everythin you encolse b/w single or double quote mark it is considered as string.
# Strings are immutable. e.g. -> It can not be changed.
name = "Dheeraj sharma"

# We can also enclose a string into triple single quote or double quote.
paragraph = '''
This is dheeraj sharma.
I am pursuing B.C.A from vikram university, ujjain.
'''

print(paragraph)

# We can loop through in a string using a for loop
for char in name:
    print(char)
    
# len function is used to find length of a string
print(len(name))

# Slicing in python
print(name[0:5]) # we can access a specific part of string using slicing. Here it will return subtring of name from index 0 to 4.


nm = "Harry"
print(nm[-4:-2]) # If we use negative index then it will treat as (length of string - index).

# String methods.
print(nm.upper()) # Converts nm to uppercase and returns a new string.
print(nm.lower()) # Converts nm to lowercase and returns a new string.
print(nm.rstrip("y")) # Removes the occurences of given string or character from the end of the string.
print(nm.replace("r", "e")) # Replaces all the occurences of given string to new string.
print(nm.split(" ")) # It will split the string by spaces and makes it list.
print(nm.capitalize()) # Turns the first character of string into uppercase and other characters to lowercase.
print(nm.center(10)) # This function adds (given number - length of string) spaces into the string.
print(nm.count("y")) # Returns the count of occurences of given string or char.
print(nm.endswith("y")) # Return true if the string is ends with given string
print(nm.find("r")) # It will return the first occurence of the given character or string otherwise -1.
print(nm.index("y")) # It will same as find but if the value is not found then it will raise an error.
print(nm.isalnum()) # return true if the string is alpha numeric.
print(nm.isalpha()) # return true if the string is alphabetic string.


# Fstrings -> We can use variables inside a string.
name = "Dheeraj"
greetings = f"Good morning {name}"
print(greetings)