inventory = {}
conditions = set()
def add(item,condition="good"):
    quantity=int(input("Enter quantity:"))
    condition=input("Input Condition 'bad' or 'good': ").lower()
    inventory[item]=(quantity,condition)
    conditions.add(condition)
def update(item):
    if item in inventory:
        quantity,condition=inventory[item]
        quantity = int(input("Enter new quantity: "))
        inventory[item]=(quantity,condition)
        print("Item Updated")
    else:
        print("Item not found")
def delete(item):
    if item in inventory:
        del inventory[item]
        print("Item Deleted")
    else:
        print("Item not found")
def search(item): 
    if item in inventory:
        quantity,condition=inventory[item]
        if quantity<=0:
            print("Out of stock")
        else:
            print("Item:",item ,"\nQuantity:",quantity ,"\nCondition:",condition)
    else:
        print("Item not found")        
def list_items():
    for item in inventory:
        quantity,condition=inventory[item]
        print("Item:",item ,"\nQuantity:",quantity ,"\nCondition:",condition)
    print("Conditions:", conditions)
       
while True:
    print("\n1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. List all Item")
    print("6. Exit")
    choice=int(input("Enter Choice: "))
    match choice:
        case 1:
            item=input("Enter item to add:").upper()
            add(item)
            print("Item Added")
        case 2:
            item=input("Enter item to update:").upper()
            update(item)
        case 3:
            item=input("Enter item to delete:").upper()
            delete(item)
        case 4:
            item=input("Enter item to Search").upper()
            print("Searching item")
            search(item)
        case 5:
            print("Listing All items:")
            list_items()
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid Option")