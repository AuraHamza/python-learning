# class parent:
#     def __init__(self):
#         self.x=10

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         self.y=20

# c=child()

# print(c.y)
# print(c.x)

# OR

# class parent:
#     def __init__(self):
#         self.x=10

# class child(parent):
#     def __init__(self):
#          self.y=20
#          self.x=10

# c=child()

# print(c.y)
# print(c.x)

# But we can directly access parent class function 

class Parent:
    def display(self):
        print("Hello")
class Child(Parent):
    pass

c = Child()
c.display()

# Summary : init apna apna 

