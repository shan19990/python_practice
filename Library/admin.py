from user import User

class Admin:
    
    def __init__(self):
        self.user = "admin"
        self.user_list = []
     
    def create_user(self):
        number_of_user = int(input("Enter the number of users in the Library: "))
        for _ in range(number_of_user):
            name = input("Enter the your name: ")
            self.user_list.append(User(name))
   
    def show_user(self):
        print("The users are :")
        for c in self.user_list:
            print(f"User:{c.user}, Books borrowed:{c.book}")
            
    def user_login(self,user):
        for u in self.user_list:
            if user in u.user:
                return u
            else:
                print("user not found")
                
    def show_books(self):
        Books.book_list()
        