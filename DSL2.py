class Bankacc: 
    def __init__(self): 
        self.balance = 0 

    def deposit(self): 
        amt = int(input("Amount to be deposited: ")) 
        self.balance += amt 
        print("Amount deposited:", amt) 

    def withdraw(self): 
        amt = int(input("Amount to be withdrawn: ")) 
        if self.balance >= amt: 
            self.balance -= amt 
            print("Amount withdrawn:", amt) 
        else: 
            print("Insufficient funds") 

    def display(self): 
        print("Net Balance:", self.balance) 

s = Bankacc() 

while True:   
    choice = int(input("Enter which operation you want to perform:\n1. Deposit\n2. Withdraw\n")) 
    if choice == 1: 
        s.deposit() 
        s.display() 
    elif choice == 2: 
        s.withdraw() 
        s.display() 
    else: 
        break


