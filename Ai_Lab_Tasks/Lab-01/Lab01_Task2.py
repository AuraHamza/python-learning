result=(["OOP",87],["SE",90],["DSA",75],["PF",66],["SRE",90],["SDA",86])
Grades={"A":0 , "B":0 ,"C":0 ,"D":0 ,"F":0}

invalid=0
count=0
total=0
for n,key in result:
    if key>100 or  key<0:
        invalid+=1
        continue
    total+=key
    count+=1
    if key>=85:
        Grade="A"
    elif key>=70 and key<=84:
        Grade="B"
    elif key>=60 and key<=69:
       Grade="C"
    elif key>=50 and key<=59:
        Grade="D"
    else:
        Grade="F" 
    Grades[Grade]+=1
    print(n,"=",key,":",Grade)
avg=total/count
print("\nGrade Summary:", Grades)
print("Invalid Entries:", invalid)
print("Average:", avg)