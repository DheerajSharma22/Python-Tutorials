f = open("myfile.txt", "r") # This method is used to open a particular file, it accepts two arguments first is name of file and second is mode in which you want to open a file.

########## FILE OPENING MODES ##########
# ‘r’ ->	Open text file for reading. Raises an I/O error if the file does not exist.
# ‘r+’ ->	Open the file for reading and writing. Raises an I/O error if the file does not exist.
# ‘w’ ->	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘w+’ ->	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘a’ ->	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘a+’ ->	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘rb’ ->	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
# ‘rb+’ ->	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
# ‘wb’ ->	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘wb+’ ->	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘ab’ ->	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
# ‘ab+’ ->	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.

print("Printing file content using read")
print(f.read()) # To print the content of a file.
f.close() # We have to close a file everytime if we had opened it.


# We can use a with statement to auto close a file
# with open("myfile2.txt", "w") as f:
#     f.write("Hello my name is dheeraj sharma")

print("\nPrinting file content using readlines")
f2 = open("myfile.txt", "r")
while True:
    line = f2.readline()
    if not line:
        break
    print(line) # To read a file line by line

# Onther same function is writeline

# seek() and tell() functions
# In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

# seek() function
# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

# with open('file.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(10)
#   # Read the next 5 bytes
#   data = f.read(5)
# tell() function
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:

# with open('file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#   # Save the current position
#   current_position = f.tell()
#   # Seek to the saved position
#   f.seek(current_position)
# truncate() function
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

# Here is an example of how to use the truncate function:

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)
# with open('sample.txt', 'r') as f:
#   print(f.read())

