class Employee:
    def work(self):
        print("Employee is working.")
class Manager(Employee):
    def work(self):
        print("\nManager is managing the task.")
class Developer(Employee):
    def work(self):
        print("\nDeveloper is developing.")
class Designer(Employee):
    def work(self):
        print("\nDesigner is designing.")

m1=Manager()
d1=Developer()
d2=Designer()

m1.work()
d1.work()
d2.work()