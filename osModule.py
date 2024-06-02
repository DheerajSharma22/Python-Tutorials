import os

if (not os.path.exists("data")): # To check wheter the folder or given path exists or not.
    os.mkdir("data") # To create a folder
    
os.rename("data", "Data") # To rename folder
# os.remove("Data") # To remove a empty folder
print(os.getcwd()) # To get current directory path
os.chdir("data") # To change from current directory
print(os.getcwd()) # To get current directory path
print(os.listdir()) # To show all directories and files inside the given directory

# And many more functions try out from documentation.
