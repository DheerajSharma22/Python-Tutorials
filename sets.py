# To create sets use curly braces
s = {2, 4, 2, 6}
print(s)

# Quick quiz
s2 = set() # Empty set is created using this syntax not this {}
print(type(s2))

# Set methods
s = {1, 3, 5}
s2 = {2, 4, 5, 6}

print(s.union(s2)) # It will return new set.
# s.update(s2)  It will update the existing set in which the function is called.
# print(s)

print(s.intersection(s2)) # It will return new set
# s.intersection_update(s2) It will update the existing set in which the function is called.
# print(s)

print(s.symmetric_difference(s2)) # Symmetric difference of two sets are those elements which are not common in both sets.