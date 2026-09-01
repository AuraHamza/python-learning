def compute_units_cost(units):
    if units<=100:
        slab_cost=units*12
    elif units<=300:
        slab_cost=(100*12)+((units-100)*18)
    else:
        slab_cost=(100*12)+(200*18)+((units-300)*25)
    return slab_cost

def compute_bill(units, tax_rate=0.17, fixed_charge=150):
    slab_cost=compute_units_cost(units)
    tax=slab_cost*tax_rate
    total=slab_cost+tax+fixed_charge
    return slab_cost, tax, fixed_charge,total

units = int(input("Enter units consumed: "))

if units >= 0:
        bill1 = compute_bill(units)
        bill2 = compute_bill(units, tax_rate=0.10)
        bill3 = compute_bill(units, tax_rate=0.20, fixed_charge=200)

        print("\n---Bill 1---")
        print("Units:", units)
        print("Slab Cost:", bill1[0])
        print("Tax:", bill1[1])
        print("Fixed Charge:", bill1[2])
        print("Total:", bill1[3])

        print("\n---Bill 2---")
        print("Units:", units)
        print("Slab Cost:", bill2[0])
        print("Tax:", bill2[1])
        print("Fixed Charge:", bill2[2])
        print("Total:", bill2[3])

        print("\n---Bill 3--")
        print("Units:", units)
        print("Slab Cost:", bill3[0])
        print("Tax:", bill3[1])
        print("Fixed Charge:", bill3[2])
        print("Total:", bill3[3])
else:
    print("Invalid input")