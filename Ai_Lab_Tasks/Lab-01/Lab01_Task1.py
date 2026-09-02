name=input("Enter name of student:")
age=int(input("Enter age:"))
cgpa=float(input("Enter CGPA:"))
courses=input("Enter Courses:").split()
#if we press space in input split take them different string and make a list from that 
profile = {
    "name": name,
    "age": age,
    "cgpa": cgpa,
    "courses": courses
}
print("\n---Student Profile---")
print("\nName:",profile["name"],"\nAge:",profile["age"],"\nCGPA:",profile["cgpa"],"\nCourses:",profile["courses"])

print("\nType of each key:")
for key in profile:
    print(key,":",profile[key],"=",type(profile[key]))