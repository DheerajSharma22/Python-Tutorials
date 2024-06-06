import os

def clearTheClutter(folderPath, extension):
    os.chdir(folderPath)
    allFiles = filter(lambda file: True if file.endswith(extension) else False, os.listdir())

    for index, file in enumerate(allFiles):
        if (file.endswith(extension)):
            os.rename(file, f"{index+1}{extension}")

            
folder = input("Enter the folder name :- ")
extension = input("Enter the file extension :- ")
    

clearTheClutter(folder, extension)