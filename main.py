class Liabrary:
    def __init__(self, listOfBooks, stName):
        self.book = listOfBooks
        self.name = stName

    def availableBook(self):
        for book in self.book:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.book:
            print(
                f"Thank You {self.name}, You have been issued {bookName}, Please keep it safe, and return it within 30 days")
            self.book.remove(bookName)
            return True
        else:
            print(
                f"Sorry {self.name} This book is not Available in the liabrary.")
            return False

    def returnBook(self, bookName):
        print(
            f"Thank You {self.name} for returnig {bookName}, have a nice day!")
        self.book.append(bookName)


class Student:

    def requestBook(self):
        self.book = input(
            "Please enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input(
            "Please enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    availLiabrary = Liabrary(
        ["Java", "Python", "Django", "JavaScript", "HTML", "CSS", "C++"], input("Please Enter Your Name: "))
    student = Student()
while (True):
    welcomeMsg = f'''\n ********Hey! {availLiabrary.name}, Welcome To The Coding Liabrary********
    Please Choose an Option
    1. List of all available Books
    2. Request for borrow a book
    3. Return/Add a book
    4. Quit
    
    '''
    print(welcomeMsg)
    option = int(input("Please Choose a option: "))
    if (option == 1):
        availLiabrary.availableBook()
    elif (option == 2):
        availLiabrary.borrowBook(student.requestBook())
    elif (option == 3):
        availLiabrary.returnBook(student.returnBook())
    elif (option == 4):
        print("Thank You for Visiting liabrary!")
        exit()
    else:
        print("Please Enter valid input!")
