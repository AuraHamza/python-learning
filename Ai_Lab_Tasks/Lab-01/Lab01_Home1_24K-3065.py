student = ('Nadeem', 28, 3.75)
#student[1] = 24  the student had a birthday
#its a tuple so the data couldnot changed after initialization 
# its a type error,
def show(name, age):
 print('Name : ', name)
 print('Age : ', age)

#show(28, 'Nadeem')
# #logical error
show('Nadeem',28)
age_entered = int(input('Enter age: '))
#python always takes input in string so i converted the type 
#into int()
if age_entered > 18:#Logical Error
  print('Adult')
marks = [90, 85, 78]
total=sum(marks)#logical error
print('Average : ', total / 3)#for better code we can also do 
#total/len(marks) for better logic 