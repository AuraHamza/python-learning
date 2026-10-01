class BankAccount:
    def __init__(self,account_holder,account_no,balance):
        self.account_holder=account_holder
        self.account_no=account_no
        self.__balance=balance
    def get_balance(self):
          return self.__balance

    def deposit(self,amount):
          self.__balance+=amount

    def display(self):
         print("Account Holder:", self.account_holder)
         print("Account No:", self.account_no)
         print("Balance:", self.get_balance())


class SavingsAccount(BankAccount):
    def __init__(self,account_holder,account_no,balance,interest_rate):
            super().__init__(account_holder, account_no, balance)
            self.interest_rate=interest_rate

    def calculate_interest(self,amount):
        amount=self.interest_rate*amount

    def display(self):
        super().display()
        print("Intersent Rate:",self.interest_rate)
    

class CurrentAccount(BankAccount):
      
    def __init__(self,account_holder,account_no,balance):
         super().__init__(account_holder, account_no, balance)

    def withdraw(self,amount):
        self._BankAccount__balance-=amount
    def display(self):
         super().display()
         print("Account Type: Current Account")


def show_account(account):
    account.display()

account1 = SavingsAccount("Hamza", 101, 5000, 10)
account2 = CurrentAccount("Noman", 102, 3000)

show_account(account1)
show_account(account2)