from gurobipy import *

# Sets
Oils = ["Veg 1", "Veg 2", "Oil 1", "Oil 2", "Oil 3"]
I = range(len(Oils))

Months = ["Jan","Feb","Mar","Apr","May","Jun"]
T = range(len(Months))

# Data
veg = ["Veg" in Oils[i] for i in I]
h = [8.8, 6.1, 2.0, 4.2, 5.0]
c = [[110, 130, 110, 120, 100,  90], 
     [120, 130, 140, 110, 120, 100],
     [130, 110, 130, 120, 150, 140], 
     [110,  90, 100, 120, 110,  80], 
     [115, 115,  95, 125, 105, 135]]
jan = [c[i][0] for i in I]

MaxV = 200
MaxN = 250
Sell = 150
MinH = 3
MaxH = 6

StoreCost = 5
StoreMax = 1000
Initial = 500

m = Model("Oil Blending")

# Variables
# X[i,t] is amount to blend
X = { (i,t): m.addVar() for i in I for t in T }
# S[i,t] is amount to store at end of month
S = { (i,t): m.addVar() for i in I for t in T }
# Y[i,t] is amount to purchase
Y = { (i,t): m.addVar() for i in I for t in T }

# Objective
m.setObjective(Sell*quicksum(X[i,t] for i in I for t in T) -
               quicksum(c[i][t]*Y[i,t] for i in I for t in T) -
               StoreCost*quicksum(S[i,t] for i in I for t in T), 
               GRB.MAXIMIZE)

# Constraints

for t in T:
    # Processing Limits
    m.addConstr(quicksum(X[i,t] for i in I if veg[i]) <= MaxV)
    m.addConstr(quicksum(X[i,t] for i in I if not veg[i]) <= MaxN)

    # Hardness limits
    m.addConstr(quicksum((h[i]-MaxH)*X[i,t] for i in I) <= 0)
    m.addConstr(quicksum((MinH-h[i])*X[i,t] for i in I) <= 0)

    for i in I:
        m.addConstr(S[i,t] <= StoreMax)
        if t > 0:
            m.addConstr(S[i,t] == S[i,t-1] + Y[i,t] - X[i,t])
        else:
            m.addConstr(S[i,0] == Initial + Y[i,0] - X[i,0])
            
for i in I:
    m.addConstr(S[i,T[-1]] >= Initial)
        
m.optimize()

print("Total profit $",m.objVal)
for t in T:
    print(Months[t])
    print("Buy", [round(Y[i,t].x,1) for i in I])
    print("Blend", [round(X[i,t].x,1) for i in I])
    print("Store", [round(S[i,t].x,1) for i in I])
    
# print("Hardness",sum(h[i]*X[i].x for i in I)/sum(X[i].x for i in I))




