# Online Library Management System.

# create a library class.
# define methods.
# method to display all the book.
# mtd to lend a book.
# mtd to add a book, if a person donates a book.
# mtd to return a book.

# gyanGhar = library(list of books, library name)

# have to maintain a dictionary of borrower and book (key - books, value - borrower name).

import sys
class Library:
    def __init__(self, bookList, libName):
        self.bookList = bookList
        self.libName = libName

    def writePreDefinedSetofBooks(self):
        f = open('BookList.txt', "r+")
        if f.read() == "":
            for book in self.bookList:
                f.write(f"{book}\n")
        f.close()

    def writeinfile(self, bookname):
        f = open("BookList.txt", "a")
        f.write(f"{bookname}\n")
        f.close()

    def display(self):
        f = open("BookList.txt", "r")
        content = f.readlines()
        content = list(map(str.strip, content))  # logic to removed the \n from the elements in the list.
        print("List of all availaible books:", content)

    def borrowerDisplay(self):
        f2 = open("BorrowerList.txt", "r")
        borrowerList = f2.readlines()
        if len(borrowerList) == 0:  # logic if no person have borrowed book, then display relevant text.
            print("No person have borrowed the books yet.")
            f2.close()
            return
        borrowerList = list(map(str.strip, borrowerList))    # logic to removed the \n from the elements in the list.
        print("Borrower list is, with book, borrower respectively: ", borrowerList)
        f2.close()

    def addBook(self):
        bookName = input("Which book you are donating: ")
        self.writeinfile(bookName)

    bookChoice = ""
    def lendBook(self):
        global bookChoice
        bookChoice = input("Name of the book you want to borrow from library: ")
        self.removeFromBookList()
        borrower = input("Your Name: ")
        dict = {bookChoice:borrower}
        f2 = open("BorrowerList.txt", "a")
        for key, value in dict.items():
            f2.write(f"{key} : {value}\n")
        f2.close()
        # f = open("")

    def removeFromBookList(self):
        with open("BookList.txt", "r") as f:
            content = [line.strip() for line in f]  # list comprehension.

        with open("BookList.txt", "w") as f:
            for book in content:
                if book != bookChoice:
                    f.write(f"{book}\n")

    def returnBook(self):
        bookName = input("Which book you are returning: ")
        borrowerName = input("Your name: ")
        with open("BookList.txt", "a") as f:
            f.write(f"{bookName}\n")
        self.removeFromBorrowerList(bookName, borrowerName)


    def removeFromBorrowerList(self, bookName, borrowerName):
        dictionaryOfBorrowBooks = {}
        with open("BorrowerList.txt", "r") as f2:
            borrowerList = [line.strip() for line in f2]  # list comprehension.
        for element in borrowerList:
            dictionaryOfBorrowBooks.update({element.split(':')[0].strip(' '): element.split(':')[1].strip(' ')})
        with open("BorrowerList.txt", "w") as f2:
            for key, value in dictionaryOfBorrowBooks.items():
                if key != bookName and value != borrowerName:
                    f2.write(f"{key} : {value}\n")

    def erase(self):
        with open("BookList.txt", "w") as f:
            f.seek(0)
            f.truncate()
        with open("BorrowerList.txt", "w") as f2:
            f2.seek(0)
            f2.truncate()


gyan_ghar = Library(["Macbeth", "lovely"],"Gyan_Ghar")

if len(gyan_ghar.bookList) !=0:
    gyan_ghar.writePreDefinedSetofBooks()

show = input("Press s to display all the books: ")
if show == "s":
    gyan_ghar.display()
    gyan_ghar.borrowerDisplay()

query = input("\nPress a to donate, b to borrow, r to return the book, t to erase data or e to exit the program: ")
if query == "a":
    gyan_ghar.addBook()
elif query == "b":
    gyan_ghar.lendBook()
elif query == 'r':
    gyan_ghar.returnBook()
elif query == "t":
    gyan_ghar.erase()
elif query == "e":
    sys.exit(1)
else:
    pass



# with open("BorrowerList.txt", "r") as f2:
#     borrowerList = [line.strip() for line in f2]

# for element in borrowerList:
#     borrowerList[element] = dict(borrowerList[element])  # TypeError: list indices must be integers or slices, not str

# borrowerList[0] = dict(borrowerList[0])   # ValueError: dictionary update sequence element #0 has length 1; 2 is required
# print(borrowerList[0])
# print(borrowerList)
#
# for element in borrowerList:
#     print(element)



# logic to build, if the book is borrowed then remove it from the book list file and add to it borrower list.
# logic - when book is returned, add it to book list and remove it from borrower list.

# flaw - when all the book are borrowed, it must show no book availaible, but it will see the condition in function
# writePreDefinedSetofBooks and program will write all the books again in the BookList.

# use coroutines.
