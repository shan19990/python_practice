from user import User

class Admin:
    
    def __init__(self,username,password):
        self.user = username
        self.password = password
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
                
    def check_if_correct_login(self,user,password):
        if self.user == user and self.password == password:
            return True
        else:
            return False
    

        