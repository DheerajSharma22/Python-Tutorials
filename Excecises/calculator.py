print("Welcome to fancy calculator.")

num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
sign = input("Choose sign from +,-,*,/ :- ")

match (sign):
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
        

