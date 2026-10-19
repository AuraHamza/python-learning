from ortools.sat.python import cp_model

def solve_exam_schedule():
    model = cp_model.CpModel()
    subjects = ["Math", "Physics", "AI", "OS", "DB"]
    exam = {}
    for s in subjects:
        exam[s] = model.NewIntVar(1, 6, s)

    model.Add(exam["Math"] != exam["Physics"])
    model.Add(exam["AI"] != exam["OS"])
    model.Add(exam["OS"] != exam["DB"])

    model.AddAbsEquality(
        model.NewIntVar(2, 6, "AI_OS_Gap"),
        exam["AI"] - exam["OS"]
    )
    model.Add(exam["Math"] < exam["DB"])
    day1 = []
    day2 = []
    day3 = []
    for s in subjects:
        d1 = model.NewBoolVar(s + "_D1")
        d2 = model.NewBoolVar(s + "_D2")
        d3 = model.NewBoolVar(s + "_D3")

        model.AddAllowedAssignments([exam[s]], [(1,), (2,)]).OnlyEnforceIf(d1)
        model.AddAllowedAssignments([exam[s]], [(3,), (4,)]).OnlyEnforceIf(d2)
        model.AddAllowedAssignments([exam[s]], [(5,), (6,)]).OnlyEnforceIf(d3)
        model.Add(sum([d1, d2, d3]) == 1)
        day1.append(d1)
        day2.append(d2)
        day3.append(d3)

    model.Add(sum(day1) <= 2)
    model.Add(sum(day2) <= 2)
    model.Add(sum(day3) <= 2)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for s in subjects:
            print(s, "-> Slot", solver.Value(exam[s]))
    else:
        print("No solution found")
solve_exam_schedule()