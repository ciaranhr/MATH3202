from gurobipy import *

# Data
profit = [10, 6, 8, 4, 11, 9, 3]
P = range(len(profit))

Machines = ["Grinding","VDrilling","HDrilling","Boring","Planing"]
n = [4, 2, 3, 1, 1]
M = range(len(n))

# usage[P][M]
usage = [
    [0.5, 0.1, 0.2, 0.05, 0.00],
    [0.7, 0.2, 0.0, 0.03, 0.00],
    [0.0, 0.0, 0.8, 0.00, 0.01],
    [0.0, 0.3, 0.0, 0.07, 0.00],
    [0.3, 0.0, 0.0, 0.10, 0.05],
    [0.2, 0.6, 0.0, 0.00, 0.00],
    [0.5, 0.0, 0.6, 0.08, 0.05]
    ]

# months
T = range(6)

# maintenance[T][M]
maint = [
    [1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1]
    ]
target = [sum(maint[t][m] for t in T) for m in M]

# market[P][T]
market = [
    [ 500, 600, 300, 200,   0, 500],
    [1000, 500, 600, 300, 100, 500],
    [ 300, 200,   0, 400, 500, 100],
    [ 300,   0,   0, 500, 100, 300],
    [ 800, 400, 500, 200,1000,1100],
    [ 200, 300, 400,   0, 300, 500],
    [ 100, 150, 100, 100,   0,  60]
    ]

maxstore = 100
storecost = 0.5
endstore = 50
initialstore = 0
monthhours = 16*24

fp = Model("Factory Planning")

# Variables
# X[p,t] is amount to make
X = { (p,t): fp.addVar() for p in P for t in T}
# Y[p,t] is amount to sell
Y = { (p,t): fp.addVar(ub=market[p][t]) for p in P for t in T}
# S[p,t] is amount to store at end of month
S = { (p,t): fp.addVar(ub=maxstore) for p in P for t in T}
# Z[t,m] number of machine m to maintain in month t
Z = { (t,m): fp.addVar(vtype=GRB.INTEGER) for t in T for m in M}

# Objective
fp.setObjective(quicksum(profit[p]*Y[p,t] for p in P for t in T) -
                quicksum(storecost*S[p,t] for p in P for t in T), GRB.MAXIMIZE)

# Constraints
for t in T:
    for m in M:
        fp.addConstr(quicksum(usage[p][m]*X[p,t] for p in P) <= monthhours*(n[m]-Z[t,m]))
    
    for p in P:
        # fp.addConstr(Y[p,t] <= market[p][t])
        # fp.addConstr(S[p,t] <= maxstore)
        if t > 0:
            fp.addConstr(S[p,t] == S[p,t-1] + X[p,t] - Y[p,t])
        else:
            fp.addConstr(S[p,0] == X[p,0] - Y[p,0])

for p in P:
    fp.addConstr(S[p,T[-1]] >= endstore)        

# ensure we do the same amount of maintenance
for m in M:
    fp.addConstr(quicksum(Z[t,m] for t in T) == target[m])

# smooth maintenance - no more than two machines per month
for t in T:
    fp.addConstr(quicksum(Z[t,m] for m in M) <= 2)
    
    
fp.optimize()

print("Total profit",fp.objVal)

print("Make")
for t in T:
    print(t,[round(X[p,t].x,1) for p in P])
print("Sell")
for t in T:
    print(t,[round(Y[p,t].x,1) for p in P])
print("Store")
for t in T:
    print(t,[round(S[p,t].x,1) for p in P])
print("Maintain")
for t in T:
    print(t,[round(Z[t,m].x) for m in M])








