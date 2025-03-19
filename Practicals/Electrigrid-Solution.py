from gurobipy import *
import math

# Set of nodes
N = range(20)

# The location of each node
nodes = {
    0: (58,88),
    1: (26,19),
    2: (21,94),
    3: (12,25), # G0
    4: (18,58),
    5: (80,66),
    6: (77,91),
    7: (61,28),
    8: (83,53),
    9: (50,83), # G1
    10: (8,92),
    11: (21,66),
    12: (67,19), # G2
    13: (57,61),
    14: (10,13),
    15: (38,88),
    16: (45,6),
    17: (95,91),
    18: (72,78),
    19: (77,33)
}

# connections between nodes
grid = [
    (7,19),(19,7),(7,13),(13,7),(4,11),(11,4),(2,11),(11,2),
    (2,10),(10,2),(11,13),(13,11),(6,18),(18,6),(17,18),(18,17),
    (6,17),(17,6),(0,6),(6,0),(0,18),(18,0),(8,19),(19,8),
    (8,13),(13,8),(7,12),(12,7),(12,16),(16,12),(12,19),(19,12),
    (1,7),(7,1),(1,14),(14,1),(1,16),(16,1),(9,13),(13,9),
    (13,18),(18,13),(0,9),(9,0),(5,18),(18,5),(5,13),(13,5),
    (5,8),(8,5),(5,17),(17,5),(1,3),(3,1),(3,14),(14,3),
    (3,4),(4,3),(11,15),(15,11),(2,15),(15,2),(9,15),(15,9)
]

# demand (MW) at each node
demand = [32,60,36,0,26,60,31,37,21,0,55,31,0,33,36,67,27,60,58,31]

# capacity (MW) and cost ($/MWh) for each generator node
capacity = { 3: 210, 9: 306, 12: 439 }
cost = { 3: 81, 9: 81, 12: 68 }

hoursrunning = 24
loss = .001

# E[i,j] gives the distance (km) from node i to node j
E = {}
for edge in grid:
    n1 = edge[0]
    n2 = edge[1]
    distance = math.hypot(nodes[n1][0]-nodes[n2][0],nodes[n1][1]-nodes[n2][1])
    E[n1,n2] = distance

    
m = Model("Electrigrid")

# Variables

# X[n] amount to generate a node n
X = { n: m.addVar() for n in N }
 
# Y[e] amount to send on edge e
Y = { e: m.addVar() for e in E }
 
# Objective
 
m.setObjective(quicksum(hoursrunning*cost[g]*X[g] for g in cost))

# Constraints

# Production
for n in N:
    if n in capacity:
        m.addConstr(X[n] <= capacity[n])
    else:
        m.addConstr(X[n] <= 0)

# Flow balance
for n in N:
    m.addConstr(X[n] + quicksum((1-loss*E[e])*Y[e] for e in E if e[1] == n) == 
                demand[n] + quicksum(Y[e] for e in E if e[0] == n))


m.optimize()

print("Total cost",m.ObjVal)
for g in cost:
    print("Generator",g,X[g].x,"MW")
    
    
    




