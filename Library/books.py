
class Books:
    all_books = []
    
    def __init__(self,book_id,title,author,published_year,is_borrowed):
        self.book_id = book_id
        self.title=title
        self.author=author
        self.published_year=published_year
        self.is_borrowed=is_borrowed
        Books.all_books.append(self)
        
    def display_info(self):
        print(f"Book Id: {self.book_id}, Title: {self.title}, Author: {self.author}, Published Year: {self.published_year}, is_borrowed: {self.is_borrowed}")
        
        
    @classmethod   
    def book_list(cls):
        for book_instance in cls.all_books:
            if not book_instance.is_borrowed:
                book_instance.display_info()
                
    @classmethod       
    def borrow_book(cls,book):
        for instance in cls.all_books:
            if instance.book_id == int(book) and not instance.is_borrowed:
                print("Available", instance.title)
                instance.is_borrowed = True
                return instance
          
    @classmethod       
    def return_book(cls,book):
        for instance in cls.all_books:
            if instance.book_id == int(book) and instance.is_borrowed:
                print("Returned", instance.title)
                instance.is_borrowed = False
                return instance
                
            
        
        
           
    