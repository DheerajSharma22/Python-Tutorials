dic = {
    "name": "Dheeraj",
    "age": 20,
    "rollNo": "22306909",
    "CGPA": 7.5
}

print(dic["name"]) # It will throw error if key not exists
print(dic.get("name")) # It will not throw error if key not exists

print(dic.keys()) # To get all keys
print(dic.values()) # To get all values

# How to iterate a dictionary
for key in dic.keys():
    print(dic[key])
    
print(dic.items())
for key, value in dic.items():
    print(f"The key is {key} and value is {value}")
    
dic1 = { "name": "Karan", "age": 23 }
dic2 = { "rollNo": 343212 }

dic1.update(dic2) # Adds the dic2 elements to dic1
print(dic1)

dic1.clear() # Makes dic1 empty

dic1.pop("name") # Remove the given key from dictionary
dic1.popitem() # Remove the last dictionary element

# del dic1 -> deletes the dic1
