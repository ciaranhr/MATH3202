from gurobipy import*

packages = [70, 90, 100 ,110, 120, 130, 150, 180, 210, 220, 250, 280, 340, 350, 400]
compartments = ["A", "B", "C", "D"]

P = range(len(packages))
C = range(len(compartments))

max = 1000

m = Model("Rockets")

#Variables
#1 if package p in compartment c, 0 if not
X = {(p, c): m.addVar(vtype=GRB.BINARY) for p in P for c in C}

#constraints
#weight limit of each compartment met
for c in C:
    m.addConstr(quicksum(X[p, c]*packages[p] for p in P) <= 1000)

#weight of reelvant compartments is equal
m.addConstr(quicksum(X[p, 0]*packages[p] for p in P) == quicksum(X[p, 3]*packages[p] for p in P))

m.addConstr(quicksum(X[p, 1]*packages[p] for p in P) == quicksum(X[p, 2]*packages[p] for p in P))

#all packages used
m.addConstr(quicksum(X[p,c]*packages[p] for p in P for c in C) == sum(packages))

#at least 3 packages in a section
for c in C:
    m.addConstr(quicksum(X[p,c] for p in P) >= 3)

m.optimize()
print(sum(packages[p] for p in P))
for c in C:
    print("comparmtent", c)
    print("weight is:", sum(X[p,c].x*packages[p] for p in P))
    for p in P:
        if X[p, c].x:
            print("has packages", p)

