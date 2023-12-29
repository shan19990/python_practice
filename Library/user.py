from books import Books

class User:
    
    def __init__(self,user):
        self.user = user
        self.book = []
        
    def borrow_book(self):
        Books.book_list()
        choice = input("Input the Book ID you want to borrow")
        self.book.append(Books.borrow_book(choice))
    
    def return_book(self):
        print("The books you borrowed:")
        for b in self.book:
            print(f"Book Id: {b.book_id} , Title: {b.title}")
        choice = input(f"Input the Book ID you want to return: ")
        self.book.remove(Books.return_book(choice))
   