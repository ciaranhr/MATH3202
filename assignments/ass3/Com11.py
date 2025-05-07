
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
    #if (t, s, y) in _pig_plan:
        #return _pig_plan[t, s, y]
    if t == 52:
        return (0, "end")
    if y == 0:
        _pig_plan[t, s, y] = (damage(t) * s) + pig_management(t + 1, s + reprod(s), y)[0], 0
    elif y > 0:
        _pig_plan[t, s, y] =  min((damage(t) * s + \
                    pig_management(t + 1, s + reprod(s) - a * trap(s), y - a)[0], a)
                    for a in range(min(5, y)))
    
    return _pig_plan[t, s, y]

print(pig_management(0, 82, 27))


