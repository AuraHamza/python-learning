def is_prime(n):
    if n<2:
     return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def digit_sum(n):
   l=len(str(n))
   sum=0
   for i in range(l):
      m=n%10
      sum+=m
      n=n//10
   return sum

def classify(n, threshold=100):

    if n < threshold:
        return "small"
    else:
        return "large"

def summarise(*numbers):
    dict={"Smallest": 0, "Largest" : 0, "Average" : 0}

    small=numbers[0]
    large=numbers[0]
    avg=0
    sum=0
    for i in numbers:
        if i<small:
            small=i
        elif i>large:
            large=i
        sum+=i
    avg=sum/len(numbers)
    dict["Smallest"]=small
    dict["Largest"]=large
    dict["Average"]=avg
    return dict


def describe(**detials):
    for name,age in detials.items():
        print(name,age)

print("\n Is Prime Func:")
n=is_prime(11)
print(n)
print("\n Is Digit Sum Func:")
p=digit_sum(1234)
print(p)
print("\n Is Classify Func:")
print(classify(50, 80))        
print(classify(50))             
print(classify(50, threshold=40)) 
print("\n Is Summarise Func:")
print(summarise(10,20,30))
print("\n Is Describe Func:")
describe(name="Nadeem", age=28)
#describe()return None 
