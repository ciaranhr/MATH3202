
def reprod(x):
    """pig reproduction"""
    if x <= 0:
        return 0
    else:
        return round(x + x*(420-x)/5000)
    
def damage(t):
    """pig damage on trees"""
    d = 2
    dt = min(abs(t-2), abs((52+t)-2), abs(t-(52+2)))
    if dt < 10:
        d += 8*(1-(dt/10)**2)**2
    dt = min(abs(t-17), abs((52+t)-17), abs(t-(52+17)))
    if dt < 7:
        d += 6*(1-(dt/7)**2)**2
    return d   

def trap(x):
    """pigs murdered for a single trap"""
    return round(.03*x)


_pig_plan = {}
"""
t weeks
s 

"""

def pig_management(t, s, y):
    if t == 52:
        return (0, "end")
    elif (t, s, y) not in _pig_plan:
        _pig_plan[t, s, y] =  min((damage(t)*s + \
                        pig_management(t+1, reprod(s)-a*trap(s), y-a)[0], a, reprod(s)-a*trap(s))
                        for a in range(min(5, y+1)))
        
    return _pig_plan[t, s, y]

def show_strategy():
    strategy = {}
    max = 51
    s = 82
    a = 27
    for t in range(max+1):
        strategy[t] = pig_management(t, s, a)[1]
        s = pig_management(t, s, a)[2] 
        a = a - strategy[t] 
        t += 1
    return strategy
        

     

print(pig_management(0, 82, 27))
trap_info = show_strategy()
trap_weeks = {key: value for key, value in trap_info.items() if value != 0}
print(trap_weeks)



