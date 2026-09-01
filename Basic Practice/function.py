def new_func():

    def greet():
        print("Welcome!")

    greet()
    greet()
    greet()

    def add(a, b):
        print("Sum of two numbers is:", a + b)

    add(5, 10)

    def round_to_two_places(num):
        return round(num, 2)


    print(round_to_two_places(3.14159))

    def autogreet(name="Hello"):
        print(name)

    autogreet()

new_func()

