class Person: # Syntax to create a class
   
    def __init__(self, name, occupation, netWorth): # Syntax to create a contructor
        self.name = name
        self.occupation = occupation
        self.netWorth = netWorth
    
    # Below is a class method or behaviour
    def printInfo(self):
        print(f"{self.name} is a {self.occupation} and its net worth is {self.netWorth}")

'''        
dheeraj = Person() # Syntax to create an object

# Here the dot(.) Operator is used to access properties and methods of an object
dheeraj.name = "Dheeraj"
dheeraj.occupation = "Software Developer"
dheeraj.netWorth = 1000000
dheeraj.printInfo()
'''

# Above code is for manually setting class properties, now we set properties using constructor
dheeraj = Person("Dheeraj", "Software Engineer", "10000000")
dheeraj.printInfo()