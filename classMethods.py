class Employee:
    # Class variable
    companyName = "Apple"
    
    # For all methods by default the first parameter is refrence to the instance in which the method is called.    
    def show(self):
        print(f"The name is {self.name} and company is {self.companyName}")

    # But if, we want to pass refrence of class. Then we can use @classmethod decorator.
    @classmethod
    def changeCompanyName(cls, newCompanyName):
        cls.companyName = newCompanyName
                
e1 = Employee()
e1.name = "Dheeraj"
# e1.show()
e1.changeCompanyName("Google")
# e1.show()
# print(Employee.companyName)


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # We can use class methods as an atlernative constructor.
    @classmethod
    def fromStr (cls, str):
        return cls(str.split(",")[0], str.split(",")[1])

p = Person("Dheeraj", 19)
print(p.name, p.age)

# Another way of creating a class instance is :- 
p2 = Person.fromStr("Neeraj,15")
print(p2.name, p2.age)