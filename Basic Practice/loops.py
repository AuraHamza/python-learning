for i in range (1,6):
    print(i)
print("\nNow, Printing Hello 5 times")
for i in range (5):
    print("Hello")

print("\nFor Loop with 3 Parameters")
for i in range(2,11,2):
    print(i)

while True:
    number = input("Enter a number: ")

    if number == "0":
        break

    print("You entered:", number)