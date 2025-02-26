from gurobipy import *

#Sets
cakes = ["chocolate", "plain"]
ingredients = ["eggs", "time", "milk"]

#set
C = range(len(cakes))
I = range(len(ingredients))

#data
revenue = [4,2]
availability = [30,480,5]
usage = [
    [4, 20, .25],
    [1,50,.2]
]

m = Model("Farmer Jones")

#Variables
X = {}
for c in C:
    X[c] = m.addVar()

#objective
m.setObjective(quicksum(revenue[c] * X[c] for c in C), GRB.MAXIMIZE) 

#constraints
for i in I:
    m.addConstr(quicksum(usage[c][i]*X[c] for c in C) <= availability[i])

m.optimize()

print("Revenue is $", m.ObjVal)
for c in C:
    print(X[c].x, cakes[c])