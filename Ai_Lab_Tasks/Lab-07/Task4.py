from ortools.sat.python import cp_model

def solve_vehicle_assignment():
    model = cp_model.CpModel()
    locations = ["L1", "L2", "L3", "L4", "L5"]
    vehicle = {}
    for l in locations:
        vehicle[l] = model.NewIntVar(1, 3, l)

    model.Add(vehicle["L1"] != vehicle["L2"])
    model.Add(vehicle["L3"] == 3)
    V1 = []
    V2 = []
    V3 = []
    for l in locations:
        a = model.NewBoolVar(l + "_V1")
        b = model.NewBoolVar(l + "_V2")
        c = model.NewBoolVar(l + "_V3")

        model.Add(vehicle[l] == 1).OnlyEnforceIf(a)
        model.Add(vehicle[l] != 1).OnlyEnforceIf(a.Not())
        model.Add(vehicle[l] == 2).OnlyEnforceIf(b)
        model.Add(vehicle[l] != 2).OnlyEnforceIf(b.Not())
        model.Add(vehicle[l] == 3).OnlyEnforceIf(c)
        model.Add(vehicle[l] != 3).OnlyEnforceIf(c.Not())
        V1.append(a)
        V2.append(b)
        V3.append(c)
    
    model.Add(sum(V1) <= 2)
    model.Add(sum(V2) <= 2)
    model.Add(sum(V3) <= 3)
    model.Add(sum(V1) - sum(V2) <= 1)
    model.Add(sum(V2) - sum(V1) <= 1)
    is_L4_V1 = model.NewBoolVar("is_L4_V1")
    model.Add(vehicle["L4"] == 1).OnlyEnforceIf(is_L4_V1)
    model.Add(vehicle["L4"] != 1).OnlyEnforceIf(is_L4_V1.Not())
    model.Add(vehicle["L5"] == 1).OnlyEnforceIf(is_L4_V1)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for l in locations:
            print(l, "-> V" + str(solver.Value(vehicle[l])))
    else:
        print("No solution found")

solve_vehicle_assignment()
