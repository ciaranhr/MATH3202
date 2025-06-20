# 2022 Q1

from gurobipy import *
    
Factories = ["A","B","C"]
Months = ["Jul","Aug","Sep","Oct","Nov","Dec"]
Grains = ["Wheat","Corn"]

F = range(len(Factories))
T = range(len(Months))
G = range(len(Grains))
H = range(5) #number of holds

Capacity = 4000
StoreCost = 1.5
Starting = [600,300]

VisitCost = 5000
ShipCost = 12000

# Demand[f][t][g]
Demand = [[[565, 290], [695, 285], [385, 315], [500, 245], [785, 270], [540, 275]], [[1050, 300], [585, 325], [510, 205], [1050, 270], [810, 210], [545, 285]], [[720, 315], [545, 465], [520, 315], [475, 465], [415, 480], [985, 525]]]

# Cost[t][g]
Cost = [[95, 43], [97, 50], [89, 76], [65, 70], [82, 49], [79, 48]]

m = Model("Shipping")

#Variables
#X is the amount of grain g to deliver to a factory f in month t
X = {(f, t, g): m.addVar() for f in F for t in T for g in G}

#X is the amount of grain g to store in factory f in month t
Y = {(f, t, g): m.addVar() for f in F for t in T for g in G}


#objective is minimising the cost for amount of grain purchased over the time period
m.setObjective(quicksum(X[f,t,g]*Cost[t][g] + Y[f,t,g]*StoreCost for f in F for t in T for g in G), GRB.MINIMIZE)


#constraints

# 
# grain purchased is not over ship cap 
for t in T:
    m.addConstr(quicksum(X[f,t,g] for f in F for g in G) <= Capacity)


#ensuring grain demand is met and linking grain storage to demand
for t in T:
    for f in F:
        for g in G:
            if t == 0:
                m.addConstr(Y[f,t,g] <= Starting[g] + X[f,t,g] - Demand[f][t][g])
            else:
                m.addConstr(Y[f,t,g] <= Y[f,t-1,g] + X[f, t, g] - Demand[f][t][g])



#initialising grain storage
for f in F:
    for g in G:
        m.addConstr(Y[f, 5, g] == Starting[g])

m.optimize()

#Z is whether the ship has arrived at factory f in month t
Z = {(f, t): m.addVar(vtype=GRB.BINARY) for f in F for t in T}

#Whether Ship is used in month t
Z1 = {t: m.addVar(vtype=GRB.BINARY) for t in T}

#if grain bought in a month for delivery, set binary variable
for t in T:
    for f in F:
        m.addConstr(quicksum(X[f,t,g] for g in G) <= Z[f,t]*4003000)

#if grain bought in a month have ship link ship variable
for t in T:
    m.addConstr(quicksum(X[f,t,g] for f in F for g in G) <= Z1[t]*1900000)

m.setObjective(quicksum(X[f,t,g]*Cost[t][g] + Y[f,t,g]*StoreCost for f in F for t in T for g in G) + quicksum(Z[f,t]*VisitCost for f in F for t in T) + quicksum(Z1[t]*ShipCost for t in T), GRB.MINIMIZE)

m.optimize()
for t in T:
    if Z1[t].x:
        print("ship used in month",Months[t])    
        #for f in F:
        #    if Z[f, t].x:
        #        print("delivery to factory", f)
    else:
        print("ship NOT used in month", Months[t])



# W is 
W = {(t, g, h): m.addVar(vtype=GRB.BINARY) for t in T for g in G for h in H}


for t in T:
    for h in H:
        m.addConstr(quicksum(W[t, g, h] for g in G) <= 1)

for t in T:
    for g in G:
        m.addConstr(quicksum(X[f, t, g] for f in F)  <= quicksum(W[t, g, h] for h in H)*800)

m.optimize()
for t in T:
    for g in G:
        for h in H:
            print(W[t, g, h].x)
            print("Grain value:", (quicksum(X[f, t, g].x for f in F)))

