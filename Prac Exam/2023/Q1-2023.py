from gurobipy import *
# Lanes
L = range(5)
midpoint = len(L)//2
L1 = L[:midpoint]
L2 = L[midpoint+1:]
multiplier = [2, 1, 0, 1, 2]
LaneLength = [40,40,40,40,35]
print("L1 and L2 ARE :", L1, L2)

# Truck types
Trucks = ["Van","Small Truck","Medium Truck","Large Truck"]
T = range(len(Trucks))
Value = [450, 600, 1000, 1800]
Length = [4.5, 7, 10, 15] # metres
Mass = [1.5, 2.5, 5, 9] # tonnes
Total = [6, 8, 7, 9] # maximum number of truck type to load
mass_cap = 120

m = Model("Relief Supplies")
# Variables
#number of trucks of type t on lane l
X = {(t, l): m.addVar(vtype=GRB.INTEGER) for t in T for l in L }

#mass on each lane
Y = {l:m.addVar() for l in L}

#objective is sum of the value of all trucks on all lanes
m.setObjective(quicksum(X[t,l]*Value[t] for t in T for l in L), GRB.MAXIMIZE)

#Constraints
#can't have more trucks then can fit on any lane
for l in L:
    m.addConstr(quicksum(X[t,l]*Length[t] for t in T) <= LaneLength[l])


#can't go over the maximum weight
m.addConstr(quicksum(X[t,l]*Mass[t] for t in T for l in L) <= mass_cap)

#can't have more trucks of type t then are available
for t in T:
    m.addConstr(quicksum(X[t,l] for l in L) <= Total[t])

#balancing loads
#Assigning each lane correct mass
for l in L:
    if l == 0 or l == 4:
        m.addConstr(Y[l] == quicksum(X[t,l]*Mass[t]*2 for t in T)) 
    elif l == 1 or l == 3:
        m.addConstr(Y[l] == quicksum(X[t,l]*Mass[t] for t in T))

m.addConstr(Y[0] + Y[1] <= 1.05*(Y[3] + Y[4]))
m.addConstr(Y[3] + Y[4] <= 1.05*(Y[0] + Y[1]))

#ensuring larger side is not more than 5%


m.addConstr 
#balance control for right side



m.optimize()

for l in L:
    for t in T:

        print("on lane:", l, "truck type:", Trucks[t], X[t, l].x)
