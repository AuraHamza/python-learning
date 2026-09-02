text=input("Enter a Text:")
vowel="aeiouAEIOU"
dict={}
vcount=0
Ccount=0
for key in text:
    if key == " ":
        continue
    if key not in dict:
        dict[key]=1
    else:
        dict[key]+=1
    if key in vowel:
        vcount+=1
    else:
        Ccount+=1
print("Vowels:",vcount)
print("Consonants:",Ccount)

print("Repeated Characters:")
for key ,n in dict.items():
    if n>1:
        print(key,":",n)
    else:
        continue

unique=set(text.replace(" ",""))
print("Unique:",unique)
print("Number of Unique Characters:",len(unique))

reverse=""
i=len(text)-1

while i>=0:
    reverse+=text[i]
    i-=1
print("Reversed:",reverse)

print("\nFirst five Slicing:",text[:5])
print("Last five Slicing:",text[-5:])
