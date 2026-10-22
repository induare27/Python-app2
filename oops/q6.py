'''Q6. Create a class BankAccount with:
Private variable __balance
Methods to deposit(amount), withdraw(amount), and get_balance()'''

class BankAccount:
    def __init__(self):
        self.__balance=5000
    def deposit(self,amount):
        self.__balance+=amount
        print(amount)
        print(self.__balance)
        print("-------------")
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(amount)
            print(self.__balance)
            print("-------------")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance

b1=BankAccount()
b1.deposit(2000)
b1.withdraw(1000)
print(b1.get_balance())

