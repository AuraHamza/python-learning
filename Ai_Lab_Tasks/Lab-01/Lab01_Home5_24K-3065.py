rules = {
    "IT Support": ["wifi", "laptop", "password"],
    "Accounts": ["fee", "payment", "refund"],
    "Library": ["book", "library", "borrow"],
    "General Office": ["document", "admission", "form"]
}
complaints = [
    ("My wifi is not working", "IT Support"),
    ("I forgot my password", "IT Support"),
    ("I want to pay my fee", "Accounts"),
    ("I need a fee refund", "Accounts"),
    ("I want to borrow a book", "Library"),
    ("The library book is missing", "Library"),
    ("I need an admission form", "General Office"),
    ("My internet connection is down", "IT Support")
]
def route(complaint, rules, fallback='General Office'):
    for department in rules:
        for keyword in rules[department]:
            if keyword in complaint:
                return department
    return fallback

correct=0
incorrect=0
department_counts={}
print("\nComplaint\t\tPredicted\t\tCorrect")
for complaint,dep in complaints:
    prediction=route(complaint,rules)
    if dep==prediction:
        correct+=1
    else:
        incorrect+=1
    if prediction not in department_counts:
        department_counts[prediction]=1
    else:
        department_counts[prediction]+=1        
    print(complaint,"\t",prediction,"\t",prediction==dep)    
accuracy=(correct/(correct+incorrect))*100

def evaluate(*results, **info):
    correct=results[0]
    incorrect=results[1]
    accuracy=results[2]
    department_counts=results[3]
    i=info
    print("\nCorrect:",correct,"\nIncorrect",incorrect,
          "\nAccuracy:",accuracy,"%","\nDepartment: ",department_counts,"\nInfo:",i)
    print(info)


evaluate(correct, incorrect, accuracy, department_counts, analyst="Khadeejah")