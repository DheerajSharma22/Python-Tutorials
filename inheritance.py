class Person:
    def __init__(self, name, email, address, phone) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
    
    def personInfo(self):
        print(f"{self.name}'s email is {self.email}, address is {self.address} and phone number is {self.phone}")

class Employee(Person): # Syntax for inheritance i.e. Employe extends Person
    def __init__(self, name, email, address, phone, employeeId, salary) -> None:
        super().__init__(name, email, address, phone) # Super function is used to call its parent class methods.
        self.employeeId = employeeId
        self.salary = salary
        
    def employeeInfo(self):
        print(f"{self.name}'s employee id is {self.employeeId} salary is {self.salary}")
        
        
e1 = Employee("Dheeraj", "ds@ds.com", "Kamal Colony", "7878787787", 102, 500000)
e1.personInfo() # An employee can use its parent function
e1.employeeInfo()
        