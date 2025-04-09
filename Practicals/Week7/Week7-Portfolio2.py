from gurobipy import *

# Part 1 (Week 4)
P = {
     "Cars Ger": 10.3,
     "Cars Jap": 10.1,
     "Comp USA": 11.8,
     "Comp Sing": 11.4,
     "App Eur": 12.7,
     "App Asia": 12.2,
     "Ins Ger": 9.5,
     "Ins USA": 9.9,
     "Short Bonds": 3.6,
     "Medium Bonds": 4.2
    }

m = Model("Portfolio")

X = {p: m.addVar() for p in P}

C = {}
C["Tot"] = m.addConstr(quicksum(X[p] for p in P)<=100000)
C["Cars"] = m.addConstr(quicksum(X[p] for p in P if "Cars" in p)<=30000)
C["Comp"] = m.addConstr(quicksum(X[p] for p in P if "Comp" in p)<=30000)
C["App"] = m.addConstr(quicksum(X[p] for p in P if "App" in p)<=20000)
C["Ins"] = m.addConstr(quicksum(X[p] for p in P if "Ins" in p)>=20000)
C["Bonds"] = m.addConstr(quicksum(X[p] for p in P if "Bonds" in p)>=25000)
C["Short/Medium"] = m.addConstr(X["Short Bonds"]>=0.4*X["Medium Bonds"])
C["Ger"] = m.addConstr(quicksum(X[p] for p in P if "Ger" in p)<=50000)
C["USA"] = m.addConstr(quicksum(X[p] for p in P if "USA" in p)<=40000)


# Part 2 (Week 7)

# Business as usual, downturn, upturn, crash
ScenarioProb = [0.8, 0.15, 0.04, 0.01]
S = range(len(ScenarioProb))

Year2Return = {
    'Cars Ger': [10.3, 5.1, 11.8, -30.0],
    'Cars Jap': [10.1, 4.4, 12.0, -35.0],
    'Comp USA': [11.8, 10.0, 12.5, 1.0],
    'Comp Sing': [11.4, 11.0, 11.8, 2.0],
    'App Eur': [12.7, 8.2, 13.4, -10.0],
    'App Asia': [12.2, 8.0, 13.0, -12.0],
    'Ins Ger': [9.5, 2.0, 14.7, -5.4],
    'Ins USA': [9.9, 3.0, 12.9, -4.6],
    'Short Bonds': [3.6, 4.2, 3.1, 5.9],
    'Medium Bonds': [4.2, 4.7, 3.5, 6.3]
}

Y = {(p, s): m.addVar() for p in P for s in S }

for p in P:
    for s in S:
        m.addConstr(Y[p,s] <= X[p] + 10000)
        m.addConstr(Y[p,s] >= X[p] - 10000)

for s in S:
    m.addConstr(quicksum(Y[p,s] for p in P) == 100000)


m.setObjective(quicksum(P[p]/100*X[p] for p in P) +
               quicksum(ScenarioProb[s] *
                        quicksum(Year2Return[p][s]/100*Y[p, s] for p in P)
                        for s in S),
                GRB.MAXIMIZE)

m.optimize()

print("\naverage earnings percentage", round(sum(P[p]/100*X[p].x for p in P)/1000,2))

for p in P:
    print(p, round(X[p].x,2))
for s in S:
    print(s, 'average earnings percentage', )