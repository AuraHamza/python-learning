class BankAccount:
    def __init__(self,account_no,account_holder,balance):
        self.account_no=account_no
        self.account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print(amount,"$ Added to account")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("not sufficent amount")
            return
        else:
            self.__balance=self.__balance-amount
        print(amount,"$ Withdraw to account")
    def get_balance(self):
        return self.__balance
    def display(self):
        print("\nAccount Number:",self.account_no)   
        print("Account Holder:",self.account_holder)
        print("Balance:$",self.__balance)

b1=BankAccount("1999","Hamza",1000)
b2=BankAccount("2921","Ali",2000)

b1.deposit(500)
b2.deposit(500)

b1.withdraw(2000)
b1.withdraw(1000)
b2.withdraw(2000)

b1.display()
b2.display()
