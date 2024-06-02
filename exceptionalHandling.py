# a = input("Enter the num: ")
# print(f"The multiplication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
# except Exception as e:
#     print(e)
    
# print("Some important lines of code")

# We can use multiple except cases.
# try:
#     num = int(input("Enter an integer: "))
#     a = [3, 6]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("Index out of bound")
    
# Use of finally
def func():
    try:
        num = int(input("Enter an integer: "))
        a = [3, 6]
        print(a[num])
        return 1
    except:
        print("Something went wrong!")        
        return 0
    finally: # It will always run whether we are returning or not from try or except.
        print("I am always executed")
        
    print("I am always excecuted") # It will not run if we are returning from try or except.
    
# func()

# Raising custom errors
# a = int(input("Enter the number between 10 and 20: "))
# if (a < 10 or a > 20):
#     raise ValueError("Value is out of range.")


# Quick quiz
a = input("Enter the num: ")
try:
    if (a == "quit"):
        pass
    else:
        a = int(a)
        print(a)
except:
    print("Entered value is not a valid integer")

