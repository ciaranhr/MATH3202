
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

def trap_check(z):
    if(z):
        return 0
    else:
        return 1

_pig_plan = {}
"""
t weeks
s 

"""

def pig_management(t, s, y, z):
    if t == 52:
        return (50*s, "end")
    elif (t, s, y, z) not in _pig_plan:
        _pig_plan[t, s, y, z] = min ((damage(t)*s + damage(t)*a*4*trap_check(z) +\
                                pig_management(t+1, reprod(s)-a*trap(s), y-a, a)[0], a)
                                for a in range(min(5, y+1)))
 

    return _pig_plan[t, s, y, z]

print(pig_management(0, 82, 27, 0))


