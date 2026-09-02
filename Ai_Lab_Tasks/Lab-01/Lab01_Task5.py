name=input("Enter your name: ")
age=int(input("Enter your age: "))
knowledge_base={
    "python":"Python is used for AI programming.",
    "grading":"Grades are based on your lab tasks and requirements.",
    "project":"The AI Lab project is based on practical AI concepts.",
    "jupyter":"Jupyter Notebook is used to write and run Python code."
}
def match_rule(question, knowledge_base):
    for keyword in knowledge_base:
        if keyword in question.lower():
            return knowledge_base[keyword]
    return None

def session_report(*questions, **stats):
    print("\nSession Report")
    print("Questions Asked:")
    for question in questions:
        print(question)
    print("Matched Rules:",stats["matched"])
    print("Unmatched Rules:",stats["unmatched"])

questions=[]
matched=0
unmatched=0
print("\nHello",name)
print("Age",age)
while True:
    question=input("Ask your question: ")
    if question.lower()=="exit":
        break
    questions.append(question)
    answer=match_rule(question,knowledge_base)
    if answer is not None:
        print(answer)
        matched += 1
    else:
        print("Sorry,I do not have an answer for that question.")
        unmatched+=1

session_report(
    *questions,
    matched=matched,
    unmatched=unmatched
)