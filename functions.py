'''
Types of arguments
1. Default
2. Keyword
3. Variable Length
4. Required Arguments
'''

# Default argument example
def defaultArgs(a = 5, b = 10): # There are no values provided for the parameters then it gets the default values.
    print(a, b)
    
defaultArgs()

# Keword and Required arg example
def calculateSum(a, b):
    sum = a + b
    return sum

# print(calculateSum()) Throws an error
print(calculateSum(10, 15))
print(calculateSum(b = 14, a = 30)) # we can pass arguments in different ordering as function receives.

# Variable length args example
def calculateAvg(*nums): # here the type of nums is tuple
    print(type(nums))
    sum = 0
    for num in nums:
       sum+=num
    return sum / len(nums) 

print(calculateAvg(5, 5, 4, 2, 6, 5))

def func(**data): # here the type of data is dictionary
    print(type(data))
    print("Hello", data["fname"], data["lname"])
    
func(fname="Dheeraj", lname="Sharma")
