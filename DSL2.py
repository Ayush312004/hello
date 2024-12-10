'''Practical No 2 
Write a Python program that computes the net amount of a bank account based a transaction 
log from console input. The transaction log format is shown as following: D 100 W 200 
(Withdrawal is not allowed if balance is going negative. Write functions for withdraw and 
deposit) D means deposit while W means withdrawal. 
Suppose the following input is supplied to the program: 
D 300, D 300 , W 200, D 100 Then, the output should be: 500'''
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

'''OUTPUT:
Enter which operation you want to perform:
1. Deposit
2. Withdraw
1
Amount to be deposited: 300
Amount deposited: 300
Net Balance: 300
Enter which operation you want to perform:
1. Deposit
2. Withdraw
1
Amount to be deposited: 300
Amount deposited: 300
Net Balance: 600
Enter which operation you want to perform:
1. Deposit
2. Withdraw
2
Amount to be withdrawn: 200
Amount withdrawn: 200
Net Balance: 400
Enter which operation you want to perform:
1. Deposit
2. Withdraw
1
Amount to be deposited: 100
Amount deposited: 100
Net Balance: 500
Enter which operation you want to perform:
1. Deposit
2. Withdraw'''

