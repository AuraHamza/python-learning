from ortools.sat.python import cp_model
model = cp_model.CpModel()
D1 = model.NewIntVar(1, 3, "D1")
D2 = model.NewIntVar(2, 3, "D2")
D3 = model.NewIntVar(1, 3, "D3")
D4 = model.NewIntVar(1, 3, "D4")

model.Add(D1 != D2)
model.Add(D3 < D4)
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Delivery Schedule:")
    print("D1:", solver.Value(D1))
    print("D2:", solver.Value(D2))
    print("D3:", solver.Value(D3))
    print("D4:", solver.Value(D4))
else:
    print("No solution found")