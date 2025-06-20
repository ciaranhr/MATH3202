N = range(10)
depot = 0
demand = [0, 3, 1, 2, 1, 2, 2, 2, 3, 2]

# dist[i][j] gives the travel time (mins) between i and j
dist = [
	[0, 30, 50, 120, 140, 180, 120, 210, 160, 100],
	[30, 0, 50, 100, 110, 160, 120, 190, 140, 70],
	[50, 50, 0, 70, 100, 130, 70, 160, 110, 60],
	[120, 100, 70, 0, 60, 60, 60, 90, 40, 30],
	[140, 110, 100, 60, 0, 120, 120, 150, 100, 40],
	[180, 160, 130, 60, 120, 0, 100, 30, 50, 90],
	[120, 120, 70, 60, 120, 100, 0, 130, 50, 90],
	[210, 190, 160, 90, 150, 30, 130, 0, 80, 120],
	[160, 140, 110, 40, 100, 50, 50, 80, 0, 70],
	[100, 70, 60, 30, 40, 90, 90, 120, 70, 0]
]
#t is time available, L is locations travelled, l is location currently located
gas = {}
def V(L, t, l):
    if dist[l][depot] > t:
        #go home instead
        gas[t, l] = (0, "home")
        return gas[t]
    else:
        return max((demand[l] + V(L+[j], t-dist[l][j], j)[0], j, L+[j], t-dist[l][j]) for j in N if j not in L)


def V_sol():
     j = depot
     L = []
     t = 360
     while True:
        v = V(L, t, j)
        if j == depot:
            print("max cylinders delivered is ", v[0])
        print("Go to", v[1])
        print("time left is: ", t)
        if v[1] == "home":
            break
        j = v[1]
        L = v[2]
        t = v[3]
     

V_sol()