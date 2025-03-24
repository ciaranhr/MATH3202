from gurobipy import *

# Sets
Oils = ["Veg 1", "Veg 2", "Oil 1", "Oil 2", "Oil 3"]
I = range(len(Oils))

T = ["January", "February", "March", "April", "May", "June"]

# Data
veg = ["Veg" in Oils[i] for i in I]
h = [8.8, 6.1, 2.0, 4.2, 5.0]
c = [[110, 130, 110, 120, 100,  90], 
     [120, 130, 140, 110, 120, 100],
     [130, 110, 130, 120, 150, 140], 
     [110,  90, 100, 120, 110,  80], 
     [115, 115,  95, 125, 105, 135]]
jan = [c[i][0] for i in I]

m = Model("Blend")

#Variables
X = { (i, t): m.addVar() for i in I for t in T}
S = { (i, t): m.addVar() for i in I for t in T}
Y = { (i, t): m.addVar() for i in I for t in T}

MaxV = 200
MaxN = 250
Sell = 150
MinH = 3
MaxH = 6

m.setObjective(quicksum((Sell - c[i][t]) * X[i] for i in I for t in T), GRB.MAXIMIZE)


m.addConstr(quicksum(X[i] for i in I if veg[i]) <= MaxV)
m.addConstr(quicksum(X[i] for i in I if not veg[i]) <= MaxN)

m.addConstr(quicksum((h[i] - MaxH) * X[i] for i in I) <=0)
m.addConstr(quicksum((MinH-h[i]) * X[i] for i in I) <=0)


m.optimize()
print("Total Profit $", m.objVal) 
for i in I:
    print(Oils[i], X[i].x)

print("Hardness", sum(h[i] * X[i].x for i in I)/sum(X[i].x for i in I))