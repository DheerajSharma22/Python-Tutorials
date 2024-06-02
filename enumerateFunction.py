fruits = ["apple", "banana", "mango", "orange", "papaya", "strawberry", "watermelon"]

for index, fruit in enumerate(fruits): # enumerate function returns a tuple of index and value
    print(fruit)
    print(f"{fruit} is favourite fruit for me") if (index == 2) else ""
    