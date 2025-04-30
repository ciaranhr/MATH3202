import numpy as np
import math
from gurobipy import *

Skills = [
    "Environmental Knowledge",
    "First Aid and CPR",
    "Communication",
    "Customer Service",
    "Law Enforcement",
    "Fire Management",
    "Navigation",
    "Maintenance Skills",
    "Education and Interpretation",
    "Wildlife Management",
    "Physical Fitness",
    "Report Writing",
    "Technical Skills",
    "Problem-Solving",
    "Public Speaking",
    "Cultural Awareness"
]


# Jobs to be completed (duration is in hours)
Jobs = [
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 2, 'duration': 5, 'day': 0 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 3, 'duration': 6, 'day': 0 },
    {'title': 'Event Planning', 'skills': [14,3,13], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3, 'day': 0 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 3, 'day': 0 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3, 'day': 0 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 0 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3, 'day': 0 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3, 'day': 0 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 2, 'day': 0 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 1 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3, 'day': 1 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3, 'day': 1 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5, 'day': 1 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2, 'day': 1 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 3, 'day': 1 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3, 'day': 1 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 1 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 4, 'day': 1 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2, 'day': 1 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 2, 'day': 1 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1, 'day': 1 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3, 'day': 1 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 1, 'duration': 2, 'day': 1 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3, 'day': 1 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 1 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4, 'day': 2 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 3, 'day': 2 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4, 'day': 2 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5, 'day': 2 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 3, 'day': 2 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 2 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 4, 'day': 2 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 4, 'day': 2 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2, 'day': 2 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 2, 'day': 2 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 4, 'day': 2 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 4, 'day': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4, 'day': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1, 'day': 3 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 2, 'duration': 5, 'day': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 3 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5, 'day': 3 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 5, 'day': 3 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4, 'day': 3 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3, 'day': 3 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2, 'day': 4 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 4 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 4 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2, 'day': 4 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 2, 'duration': 5, 'day': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2, 'day': 4 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3, 'day': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3, 'day': 4 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 4 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 3, 'day': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4, 'day': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5, 'day': 4 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 3, 'day': 4 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 1, 'day': 4 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 4, 'day': 5 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 3, 'day': 5 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 2, 'day': 5 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4, 'day': 5 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 5, 'day': 5 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 2, 'day': 5 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2, 'day': 5 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4, 'day': 5 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 5 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 4, 'day': 5 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4, 'day': 6 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 1, 'duration': 5, 'day': 6 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4, 'day': 6 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2, 'day': 6 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 1, 'duration': 6, 'day': 6 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 1, 'duration': 3, 'day': 6 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4, 'day': 6 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 6 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5, 'day': 6 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 1, 'duration': 3, 'day': 6 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 4, 'day': 6 }
]

# Skill scores for each ranger
Rangers = [
    [8,0,7,20,7,5,8,7,4,1,10,8,5,9,2,7],
    [1,19,1,11,2,11,6,10,7,6,2,2,11,0,2,9],
    [6,12,8,7,3,0,2,16,10,12,12,3,10,9,2,0],
    [3,2,6,0,12,7,4,5,18,8,14,9,4,0,7,12],
    [4,9,5,2,0,16,7,0,12,0,16,6,12,9,10,3],
    [8,0,4,0,5,11,2,9,7,12,10,5,1,14,2,14],
    [5,13,8,2,19,0,10,8,10,11,0,3,0,3,12,6],
    [2,18,3,4,1,16,14,2,9,5,3,5,11,4,0,5],
    [3,16,19,7,12,4,8,14,12,8,0,2,0,2,5,1],
    [7,18,12,4,11,5,17,0,2,4,7,4,12,3,5,0],
    [19,7,4,9,5,11,5,12,3,7,0,11,5,8,3,0],
    [10,1,12,3,1,0,6,9,2,9,0,12,10,0,16,14],
    [0,6,10,2,18,10,0,2,12,2,10,10,0,8,12,6],
    [1,2,11,1,2,3,4,20,16,0,11,16,0,0,7,18],
    [19,5,8,5,7,10,11,6,2,0,5,4,16,3,6,0],
    [12,10,5,4,0,8,9,10,6,8,14,10,2,0,8,4],
    [4,12,9,19,7,14,6,5,3,0,5,4,0,3,12,7],
    [0,1,11,12,1,17,5,9,18,2,0,4,4,6,2,9],
    [11,10,4,4,2,20,1,13,11,9,3,0,0,1,8,12],
    [10,5,0,5,16,6,3,4,0,0,10,15,0,15,10,10],
    [7,6,0,20,5,8,17,5,3,10,6,12,4,4,0,4]
]

S = range(len(Skills))
J = range(len(Jobs))
R = range(len(Rangers))

#Other Data
# Working Limits
tot_hours = 36  #Maximum workable hours during a week 
u = 10          #Maximum workable hours per day
max_days = 5    #Maximum number of day rangers can work in a week

Days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
T = range(len(Days))


clashes = [(10,11), (5,15), (8,16), (14,15)]

#List of rangers who cannot work two days in a row
family = [2, 3, 6, 12, 18]

#Binary variable mapping each skill to each job
Y = np.zeros((len(J),len(S)))
#loop through rows of Y (Jobs)
for j in J:
    #loop through columns of Y (Skills)
    for s in S:
        if s in Jobs[j]['skills']:
            Y[j,s] = 1
    
    

m = Model("Brolga")

###    VARIABLES    ###
# Allocation of Rangers: 1 if ranger r is allocated to job j on day t, else 0
X = {(r,j,t): m.addVar(vtype=GRB.BINARY) for r in R for j in J for t in T }
# Days rangers work: 1 if ranger r works on day t, else 0
Z = {(r,t): m.addVar(vtype=GRB.BINARY) for r in R for t in T}
#Add a binary variable y(r,t) if ranger works on day t (look at z variable in juice example)

###    OBJECTIVE    ###
# Maximise Skill Points
m.setObjective(quicksum(X[r,j,t]*Y[j,s]*Rangers[r][s] for j in J for r in R for t in T for s in S),GRB.MAXIMIZE)

###    CONSTRAINTS    ###
for t in T:
    #For each day the following constraints hold
    for j in J:
        
        # Avoid kinship clashing rangers working the same job
        for clash in clashes:
            m.addConstr(X[clash[0],j,t] + X[clash[1],j,t] <= 1.9)   
      
        # Jobs can only be allocated on the correct day
        if t == Jobs[j]['day']:
            # Correct number of ranger allocated to each jo
            m.addConstr(quicksum(X[r,j,t] for r in R) == Jobs[j]['rangers'])
        
        else:
            # Jobs aren't allocated on the wrong day
            m.addConstr(quicksum(X[r,j,t] for r in R) == 0)
            
       
    for r in R:        
        #Rangers do not exceed maximum workable hours per day
        m.addConstr(quicksum(X[r,j,t]*Jobs[j]['duration'] for j in J) <= u*Z[r,t])
        
    for r in family:
        m.addConstr(Z[r,T[t-1]] + Z[r, t] <= 1.9)       
        #Link Y variable with X variable
        #m.addConstr(Y[r,t]< X[r,j,t])
        
for r in R:    
    # Rangers do not exceed total number of workable hours
    m.addConstr(quicksum(X[r,j,t]*Jobs[j]['duration'] for j in J for t in T) <= tot_hours)
    # Rangers do not exceed maxiumum number of workable days
    m.addConstr(quicksum(Z[r,t] for t in T) <= max_days)

m.optimize()

print("Maximum Total Skill Points",m.ObjVal)
