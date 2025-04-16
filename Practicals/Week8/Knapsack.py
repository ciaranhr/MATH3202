import math

#KNAPSACK

#Stages: Items, j
#State: volume available, s_j
#Action: pack a_j, items of type j
#Value function: V_j(s_j) is max value from packing items of type j, ..., 3
#wtih s_j units of volume available
#we want V_1(20)

size = {1:7, 2:4, 3:3}
value = {1:25, 2:12, 3:8}

def knapsack(j, s):
    if j not in size:
        return (0, 0, None)
    else:
        max_value = (0, 0, None)
        for a in range(s//size[j] + 1):
            v = (value[j] * a + knapsack(j + 1, s - size[j] * a)[0])
            if v > max_value[0]:
                max_value = (v, a, s- size[j] * a)
        return max_value

print(knapsack(1, 20))
