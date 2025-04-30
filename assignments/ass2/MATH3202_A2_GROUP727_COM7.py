"""
Created on Wed Mar 12 15:22:32 2025

MATH3202_A2
Brolga Fire Management: Ranger Allocation

KOBI WICKENS
CIARAN HUANG-RYAN
SACHITH PANDITHA 
"""
from gurobipy import *
import math
import numpy as np

###    DATA    ###
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
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 2 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 4 },
    {'title': 'Event Planning', 'skills': [14,3,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 2, 'duration': 7 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 2 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 3 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 5 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 2 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 1, 'duration': 5 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 2 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 2 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 0 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 3, 'duration': 6 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 4 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 4 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 5 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 1, 'duration': 4 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 2 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 4 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 4 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 4 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 4 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 1, 'duration': 4 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 4 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 1, 'duration': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 2 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 5 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 4 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 2, 'duration': 4 }
]

sorted_jobs = sorted(Jobs, key=lambda x:x['title'])

# Skill scores for each ranger
Rangers = [
    [1,0,9,11,20,8,5,9,4,6,0,7,1,2,3,18],
    [0,6,9,4,0,3,6,8,19,0,13,8,4,12,6,14],
    [19,7,3,6,7,1,5,6,6,0,8,4,9,5,12,8],
    [3,7,0,1,6,0,8,7,13,0,18,7,11,4,7,19],
    [14,16,7,6,12,3,1,0,12,2,4,1,11,11,7,2],
    [1,8,0,6,7,6,1,14,1,7,6,0,9,10,16,12],
    [0,9,16,6,11,3,0,0,18,10,0,4,5,10,8,11],
    [0,3,9,0,0,11,7,0,8,11,8,17,8,7,8,18],
    [11,3,16,2,0,0,6,9,12,12,4,8,8,11,5,8],
    [0,1,0,8,6,10,8,10,0,17,3,4,8,13,12,9],
    [0,4,4,13,4,2,2,7,14,11,13,0,5,4,17,8],
    [2,19,10,6,7,20,9,1,5,1,0,2,2,0,5,10],
    [0,13,7,9,7,14,18,2,2,2,12,3,0,1,3,12],
    [11,4,8,5,10,16,7,1,2,8,9,5,1,3,7,8],
    [8,16,5,15,12,9,6,4,1,7,1,1,7,7,1,2],
    [0,6,0,3,13,8,11,0,10,8,9,5,3,4,10,18],
    [0,5,0,9,5,4,15,7,0,18,16,0,1,14,12,1],
    [0,8,13,16,9,13,4,2,1,1,2,1,0,13,13,3],
    [3,3,16,8,10,4,12,2,0,2,7,17,6,4,12,6],
    [0,16,3,1,0,16,0,8,18,5,2,16,16,4,0,10],
    [0,8,15,0,8,19,11,5,3,8,4,18,2,8,6,0]
]

S = range(len(Skills))
J = range(len(Jobs))
R = range(len(Rangers))

#Other Data
tot_hours = 36

#Binary variable mapping each skill to each job
Y = np.zeros((len(J),len(S)))
#loop through rows of Y (Jobs)
for j in J:
    #loop through columns of Y (Skills)
    for s in S:
        if s in sorted_jobs[j]['skills']:
            Y[j,s] = 1

#List of tuples each containing two ranger wo cannot work the same job
clashes = [(17,18), (2,4), (12,15), (8,13)]

m = Model("Brolga")
###    VARIABLES    ###
# Allocation of Rangers: 1 if ranger r is allocated to job j, else 0
X = {(r,j): m.addVar(vtype=GRB.BINARY) for j in J for r in R }
#Y = {(s,j): m.addVar(vtype=GRB.BINARY) for j in J for s in S}

###    OBJECTIVE    ###
# Maximise Skill Points
m.setObjective(quicksum(X[r,j]*Y[j,s]*Rangers[r][s] for j in J for r in R for s in S),GRB.MAXIMIZE)


###    CONSTRAINTS    ###
for j in J:
    # Correct number of ranger allocated to each job
    m.addConstr(quicksum(X[r,j] for r in R) == sorted_jobs[j]['rangers'])
   
    # Avoid kinship clashing rangers working the same job
    for clash in clashes:
        m.addConstr(X[clash[0],j] + X[clash[1],j] <= 1.9)   

  
    
for r in R:    
    # Rangers do not exceed total number of workable hours.
    m.addConstr(quicksum(X[r,j]*sorted_jobs[j]['duration'] for j in J) <= tot_hours)
    

m.optimize()

print("Maximum Total Skill Points",m.ObjVal)

### ERROR CHECKING/ EXTRA INFO ###
# CLASHES
for j in J:
    for clash in clashes:
        C = X[clash[0],j].x + X[clash[1],j].x 
    print(sorted_jobs[j]['title'], "clash total is:", C)

#ALLOCATION OF JOBS
for j in J:
    rangers_alocated = []
    for r in R:
        if X[r,j].x == 1:
            rangers_alocated.append(r)
    print(sorted_jobs[j]['title'], ":", rangers_alocated)

#ALLOCATION OF HOURS
workable_hours = 0
for j in J:
    workable_hours += sorted_jobs[j]['rangers']*sorted_jobs[j]['duration']
    

rangers_hours = {}
tot_hours_worked = 0
for r in R:
    hours_worked = 0
    for j in J:
        hours_worked += X[r,j].x*sorted_jobs[j]['duration']
    tot_hours_worked += hours_worked
    rangers_hours[r] = hours_worked 
print("Workable Hours", workable_hours, "Total Hours Worked", tot_hours_worked)

print(sorted(rangers_hours.items(), key= lambda x:x[1]))
print((0+5+7+12+17+17+24)/7)