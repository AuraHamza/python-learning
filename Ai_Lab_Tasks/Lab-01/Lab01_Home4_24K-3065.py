
def triangle(n):
    for i in range(1,n+1):
        for m in range(1,i+1) :
            print(m,end="") 
        print()       

# n=int(input("Enter a Number:"))
# triangle(n)        

def multiplication_table(*numbers):
    for i in range(len(numbers)):
        m=numbers[i]
        print("\nTable of:",m)
        for n in range(1,11):
            print("",m ,"x",n,":",m*n)

# multiplication_table(2,5)

def fibonacci(limit):
    numbers=[]
    n=0
    m=1
    old_n=n
    while n<limit:
        numbers.append(n)
        old_n=n
        n=n+m
        m=old_n
    return numbers

# num=fibonacci(5)
# print("fibonacci series:",num)

def collatz(n):
    step=0
    while n>1:
        if n%2==0:
            n=n//2
        else:
            n=(3*n)+1
        step+=1    
    return step        
    
# new=collatz(6)
# print("Collatz step:",new)

while True:
    print("\n1. Triangle")
    print("2. Multiplication Table")
    print("3. Fibonacci")
    print("4.  Collatz")
    print("5. Exit")
    choice=int(input("Enter Choice: "))
    match choice:
        case 1:
            n=int(input("Enter number of rows: "))
            triangle(n)
        case 2:
            multiplication_table(2, 5, 7)
        case 3:
            limit=int(input("Enter limit: "))
            print("Fibonacci:", fibonacci(limit))
        case 4:
            n=int(input("Enter number: "))
            print("Collatz steps:", collatz(n))
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid Option")