from slot import Slot

class User:
    def __init__(self,name):
        self.balance = 0
        self.line = 0
        self.bet_amt = 0
        self.total_bet_amt = 0
        self.name = name
        
    
    def deposit(self):
        while True:
            balance = input(f"Hi {self.name}, How much would you like to deposit: $")
            if balance == "exit":
                break
            elif balance.replace('.', '', 1).isdigit() and float(balance) > 0:
                self.balance += int(balance)
                print(f"You have deposited ${self.balance}")
                break
            else:
                print(f"Please select a correct value")
                
    def show_balance(self):
        print(f"Your Current balance is: ${self.balance}")
    
    def pick_lines(self):
        while True:
            line = input("How many lines would you like to play with: ")
            if line.isdigit():
                self.line = int(line)
                print(f"You have selected {self.line} lines")
                break
            else:
                print(f"Please select a correct value")
    def bet_amount(self):
        while True:
            bet_amt = input("How much would you like to bet: $")
            if bet_amt.replace('.', '', 1).isdigit() and float(bet_amt) > 0 :
                if float(bet_amt) >= self.balance:
                    print("insufficient amount")
                    self.deposit()
                else:
                    self.bet_amt = int(bet_amt)
                    print(f"You have bet ${self.bet_amt} amonst {self.line} lines")
                    self.balance -= self.bet_amt
                    break
            else:
                print(f"Please select a correct value")
      
    def spin_slot(self):
        self.instance_of_Slot = Slot(self)
        self.balance += self.instance_of_Slot.spin_slot()
        print("You have: ",self.balance)
       