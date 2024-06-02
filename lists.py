marks = [56, 75, 23, 50,48]
print(marks)

ls = [56, "dheeraj", True] # List can store different data type values
print(ls[0:3]) # We can slice the list
print(ls[1:3])

if ("dheeraj" in ls): # We can check for an element in ls using in keyword and it also works with strings.
    print("Yes")
else:
    print("No")
    
# List comprehension -> List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
ls = [i for i in range(4)]
print(ls)

# Methods of list
ls.append(-1) # Appends an element at last of list
print(ls)

ls.sort() # Sort the given list
print(ls)

ls.sort(reverse=True) # Sort the given list in reverse order or decreasing order
print(ls)

ls.reverse() # Reverses the give list
print(ls)

print(ls.index(2)) # Gives the index of given element
print(ls.count(3)) # Returns the count of given element


ls2 = ls # It will not create a copy of ls it refrences to ls
ls2 = ls.copy() # It will copy the ls list to ls2
ls2.insert(1, 899) # Insert 899 at index no. 1
m = [900, 1000, 1100]
ls2.extend(m) # extends the elements of m in ls2



