#Q2. Create a class BankAccount with attributes name and balance, and methods deposit and withdraw.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,deposit):
        self.balance+=deposit
        print(self.balance)
    def withdraw(self,withdraw):
        if withdraw<=self.balance:
            self.balance-=withdraw
            print(self.balance)
        else:
            print("Insufficient balance")
b1=BankAccount("Priya",5000)
b1.deposit(2000)
b1.withdraw(1000)
