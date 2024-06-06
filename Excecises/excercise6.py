import time

class Library:
    def __init__(self) -> None:
        self.no_of_books = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.no_of_books+=1
        
    def totalBooks(self):
        return self.no_of_books
    
    def returnIssuedBook(self, name, author):
        isBookFound = False
        for book in self.books:
            # Find the book
            if (book.name == name and book.author == author):
                isBookFound = True
                if (book.issuedTo == None): # Check if the book is not issued by the library.
                    print(f"\nThe Book {book.name} is not issued to anyone by the library.")
                    return
                else: # Now if the book is issued by the library then return it.                    
                    book.issuedTo = None
                    print("\nBook returned successfully.")
                    return

        if (not isBookFound):
            print("\nBook not found")

                
    def issueBook(self, name, author, issuedTo):
        isBookFound = False
        for book in self.books:
            # Find the book
            if (book.name == name and book.author == author):
                isBookFound = True
                # Check if the book is available or not.
                if (book.issuedTo == None):
                    # If available then issue it.
                    book.issuedTo = issuedTo
                    book.issuedOn = time.time
                else:
                    # If not available then return message
                    print("\nBook is not available.")

        if (not isBookFound):
            print("\nBook not found")
    
    def printAvailableBooks(self):
        isBookAvailable = False
        for book in self.books:
            # Check if the book is available or not.
            if (book.issuedTo == None):
                isBookAvailable = True
                print(f"\nBook name is {book.name} and Author name is {book.author}")

        if (not isBookAvailable):
            print("\nThere are no books available.")
               
class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.issuedTo = None
        self.issuedOn = None
        
print("Welcome to Library Management System.")
inp = int(input('''1 for add book to the library\n2 for return issued book\n3 for issue book\n4 for check total no of books\n5 for printing available books\n6 for exit\n'''))

# Creating the instance of library
library = Library()

while (inp != 6):
    if inp == 1:
        bookName = input("\nEnter the name of the book you want to add :- ")
        bookAuthor = input("Enter the author of the book :- ")  
        library.addBook(Book(bookName, bookAuthor))
    elif inp == 2:
        bookName = input("\nEnter the name of the book you want to return :- ")
        bookAuthor = input("Enter the author of the book :- ")
        library.returnIssuedBook(bookName, bookAuthor)
    elif inp == 3:
        bookName = input("\nEnter the name of the book you want to issue :- ")
        bookAuthor = input("Enter the author of the book :- ")
        issuedTo = input("Enter the name of the person to whom the book is to be issued :- ")
        library.issueBook(bookName, bookAuthor, issuedTo)
    elif inp == 4:
        print(f"\nThere are total {library.totalBooks()} books")
    elif inp == 5:
        library.printAvailableBooks()
    else:
        print("\nWrong input")
        break
        
    inp = int(input('''\n1 for add book to the library\n2 for return issued book\n3 for issue book\n4 for check total no of books\n5 for printing available books\n6 for exit\n'''))


