from ortools.sat.python import cp_model
def solve_course_timetabling():
    model = cp_model.CpModel()
    courses = ["CS101", "CS102", "AI201", "DS202", "SE301", "ML401"]
    students = [35, 50, 45, 60, 30, 80]
    capacity = [40, 60, 100]
    timeslot = {}
    room = {}
    for c in courses:
        timeslot[c] = model.NewIntVar(1, 4, "time_" + c)
        room[c] = model.NewIntVar(1, 3, "room_" + c)

    for i in range(6):
        allowed = []
        for r in range(3):
            if students[i] <= capacity[r]:
                allowed.append(r + 1)
        model.AddAllowedAssignments([room[courses[i]]], [(r,) for r in allowed])

    model.Add(timeslot["CS101"] != timeslot["CS102"])
    model.Add(timeslot["CS102"] != timeslot["AI201"])
    model.Add(timeslot["AI201"] != timeslot["ML401"])
    model.Add(timeslot["DS202"] != timeslot["SE301"])

    for i in range(6):
        for j in range(i + 1, 6):
            c1 = courses[i]
            c2 = courses[j]
            model.AddForbiddenAssignments(
                [timeslot[c1], room[c1], timeslot[c2], room[c2]],
                [(t, r, t, r) for t in range(1, 5) for r in range(1, 4)]
            )
    model.Add(timeslot["ML401"] >= 3)
    model.Add(timeslot["DS202"] <= 2)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for c in courses:
            print(c, "Time Slot:", solver.Value(timeslot[c]),
                  "Room: R", solver.Value(room[c]))
    else:
        print("No solution found")

solve_course_timetabling()
