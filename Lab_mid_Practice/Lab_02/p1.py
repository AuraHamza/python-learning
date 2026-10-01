class Student:
    name="Hamza Salahuddin"
    age=21
    department="SE"
Student1=Student

print("Name:",Student1.name)
print("Age:",Student1.age)
print("Department:",Student1.department)



class Student:
    name="Hamza Salahuddin"
    age=21
    department="SE"
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Department:",self.department)

Student1=Student()
Student1.display()

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=Employee("Hamza","21")
e2=Employee("Babar",34)
print("Name:",e1.name,"Age",e1.age)
print("Name:",e2.name,"Age",e2.age)

class Bank_Accounts:
    def __init__(self,holder_name,account_no,balance,bank_name):
        self.holder_name=holder_name
        self.account_no=account_no
        self.balance=balance
        self.bank_name=bank_name

    def display(self):
        print("\nName:",self.holder_name)
        print("Account NO:",self.account_no)
        print("Balance:",self.balance)
        print("Bank_name:",self.bank_name)

    def Deposite(self,amount):
        self.balance+=amount
        print("\nDeposited Amount:",amount)
        print("Balance:",self.balance)


a1=Bank_Accounts("Hamza",1,1000,"Meezan")
a2=Bank_Accounts("Noman",2,2000,"Meezan")

a1.display()
a2.display()

a1.Deposite(400)

