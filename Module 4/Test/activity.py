class Book:
    def __init__(self,title,author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("The book has been borrowed")
        else:
            print("The book has already been borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("The book has been returned")
        else:
            print("The book was never borrowed")
            

book_ob1 = Book("Harry Potter", "J.K. Rowling")
book_ob1.borrow()
book_ob1.return_book()