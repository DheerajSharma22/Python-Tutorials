print(__name__) # Prints __main__ if it is executed from the file iteself else prints file name
if __name__ == "__main__": # this check is used to stop executing main program statements when you import this file in another file.
    print("Hello")