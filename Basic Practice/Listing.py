#Negative Listing 
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])

#Positive Listing
print("\n")
numbers = [10, 20, 30, 40, 50]

print(numbers[1])
print(numbers[2])

print("\nNumber Through Loop")
a = [10,20,30,40,50]

for b in a:
    print(b)

print("\n Learing matrix or 2d-array ")
teams = [
    ["Ali", "Ahmed", "Hamza"],
    ["John", "Paul", "George"],
    ["A", "B", "C"]
]
print(teams[-1][1])


print("\n Learing iteration along the listing  ")
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

a = len(party_attendees) // 2
b = len(party_attendees) - 1

for i in range(a, b):
    print(party_attendees[i])
    